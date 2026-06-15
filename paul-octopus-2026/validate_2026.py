import ast
import csv
import importlib.util
import sys
from pathlib import Path

import numpy as np
import pandas as pd


REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = REPO_ROOT / 'paul-octopus-2026'
SUBMITTED_DIR = REPO_ROOT / 'paul-octopus-python_submited'
PRE_PROCESSING_DIR = REPO_ROOT / 'paul_octopus_pre_processing_2'
DATASET_DIR = DATA_DIR / 'datasets' / 'all_score' / '48_or_4_year'
CUTOFF_DATE = pd.Timestamp('2026-06-11')
MAX_SCORE = 8

sys.path.insert(0, str(PRE_PROCESSING_DIR))
sys.path.insert(0, str(SUBMITTED_DIR))

import constants.params as params
import constants.team_aliases as pre_processing_aliases
from utils.csv import read_historical_results


def load_module(module_name, path):
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


submitted_aliases = load_module('submitted_team_aliases', SUBMITTED_DIR / 'utils' / 'team_aliases.py')


def read_dict_csv(path):
    with open(path, newline='', encoding='utf-8') as fp:
        return list(csv.DictReader(fp))


def normalize(team):
    return pre_processing_aliases.normalize_team_name(team)


def parse_features(path):
    raw_text = path.read_text(encoding='utf-8')
    raw_text = raw_text.replace('array(', '').replace(')', '')
    return ast.literal_eval(raw_text)


def assert_true(condition, message, errors):
    if not condition:
        errors.append(message)


def validate_aliases(errors):
    assert_true(
        pre_processing_aliases.TEAM_ALIASES == submitted_aliases.TEAM_ALIASES,
        'Alias maps differ between preprocessing and submitted app.',
        errors,
    )

    expected_aliases = {
        'USA': 'United States',
        'Czechia': 'Czech Republic',
        'Curacao': 'Curaçao',
        'Cabo Verde': 'Cape Verde',
        'China': 'China PR',
        "Côte d'Ivoire": 'Ivory Coast',
    }

    for source_name, expected_name in expected_aliases.items():
        assert_true(
            normalize(source_name) == expected_name,
            f'Alias {source_name!r} should normalize to {expected_name!r}.',
            errors,
        )


def validate_results_and_samples(errors):
    results = pd.read_csv(DATA_DIR / 'results.csv', parse_dates=['date'])
    wc_2026 = results[
        (results['tournament'] == 'FIFA World Cup')
        & (results['date'].dt.strftime('%Y') == '2026')
    ].sort_values('date').reset_index(drop=True)
    wc_2022 = results[
        (results['tournament'] == 'FIFA World Cup')
        & (results['date'].dt.strftime('%Y') == '2022')
    ]

    assert_true(len(wc_2026) == 72, f'Expected 72 World Cup 2026 matches, found {len(wc_2026)}.', errors)
    assert_true(len(wc_2022) == 64, f'Expected 64 World Cup 2022 matches, found {len(wc_2022)}.', errors)
    assert_true(
        not wc_2022[['home_score', 'away_score']].isna().any().any(),
        'World Cup 2022 rows must have complete scores for validation.',
        errors,
    )

    sample_2026 = read_dict_csv(DATA_DIR / 'sample_predictions_submission.csv')
    submitted_sample = read_dict_csv(SUBMITTED_DIR / 'sample_predictions_submission.csv')

    assert_true(sample_2026 == submitted_sample, '2026 and submitted sample files are not identical.', errors)
    assert_true(len(sample_2026) == len(wc_2026), 'Sample row count does not match results.csv 2026 matches.', errors)

    sample_pairs = [(row['home'], row['away']) for row in sample_2026]
    result_pairs = [(row.home_team, row.away_team) for row in wc_2026.itertuples(index=False)]
    assert_true(sample_pairs == result_pairs, 'Sample match order/pairs do not match results.csv 2026 rows.', errors)

    schedule = read_dict_csv(DATA_DIR / 'matches-schedule.csv')
    schedule_pairs = {(row['country1'], row['country2']) for row in schedule}
    assert_true(
        schedule_pairs == set(result_pairs),
        'matches-schedule.csv does not contain the same 2026 match pairs as results.csv.',
        errors,
    )

    sample_teams = {normalize(team) for row in sample_2026 for team in (row['home'], row['away'])}
    expected_teams = {normalize(team) for team in params.C_2026_WC[1]}
    assert_true(sample_teams == expected_teams, 'Sample teams differ from C_2026_WC teams.', errors)
    assert_true(len(sample_teams) == 48, f'Expected 48 unique sample teams, found {len(sample_teams)}.', errors)


def validate_app_history_cutoff(errors):
    history = read_historical_results()

    assert_true(not history.empty, 'Submitted app historical data is empty.', errors)
    assert_true(
        history['date'].max() < CUTOFF_DATE,
        f'Submitted app history must be before {CUTOFF_DATE.date()}.',
        errors,
    )
    assert_true(
        not history[['home_score', 'away_score']].isna().any().any(),
        'Submitted app history should not contain empty scores.',
        errors,
    )


def validate_datasets_and_features(errors):
    train_path = DATASET_DIR / 'dataset_train.txt'
    test_path = DATASET_DIR / 'dataset_test.txt'
    features_path = DATASET_DIR / 'dataset_2026.txt'

    for path in [train_path, test_path, features_path]:
        assert_true(path.exists(), f'Missing dataset file: {path}', errors)

    if errors:
        return

    train = np.loadtxt(train_path, delimiter=';')
    test = np.loadtxt(test_path, delimiter=';')
    features = parse_features(features_path)

    assert_true(train.shape == (640, 11), f'Expected train shape (640, 11), found {train.shape}.', errors)
    assert_true(test.shape == (128, 11), f'Expected test shape (128, 11), found {test.shape}.', errors)
    assert_true(np.isfinite(train).all(), 'Train dataset contains non-finite values.', errors)
    assert_true(np.isfinite(test).all(), 'Test dataset contains non-finite values.', errors)
    assert_true(set(np.unique(train[:, -1])).issubset(set(range(MAX_SCORE + 1))), 'Train labels exceed expected score classes.', errors)
    assert_true(set(np.unique(test[:, -1])).issubset(set(range(MAX_SCORE + 1))), 'Test labels exceed expected score classes.', errors)

    expected_teams = {normalize(team) for team in params.C_2026_WC[1]}
    assert_true(set(features.keys()) == expected_teams, 'Feature teams differ from C_2026_WC teams.', errors)

    for team, values in features.items():
        values = np.asarray(values)
        assert_true(values.shape == (5,), f'Feature vector for {team} should have shape (5,), found {values.shape}.', errors)
        assert_true(np.isfinite(values).all(), f'Feature vector for {team} contains non-finite values.', errors)


def validate_predictions(errors):
    predictions_path = SUBMITTED_DIR / 'predictions.csv'

    if not predictions_path.exists():
        return

    predictions = read_dict_csv(predictions_path)
    sample = read_dict_csv(SUBMITTED_DIR / 'sample_predictions_submission.csv')
    expected_columns = {'home', 'home_score', 'away_score', 'away'}

    assert_true(predictions, 'predictions.csv exists but is empty.', errors)
    assert_true(set(predictions[0].keys()) == expected_columns, 'predictions.csv has unexpected columns.', errors)
    assert_true(len(predictions) == len(sample), 'predictions.csv row count does not match sample file.', errors)

    for index, (prediction, sample_row) in enumerate(zip(predictions, sample), start=1):
        assert_true(
            prediction['home'] == sample_row['home'] and prediction['away'] == sample_row['away'],
            f'Prediction row {index} teams do not match sample row.',
            errors,
        )

        for score_field in ['home_score', 'away_score']:
            try:
                score = int(prediction[score_field])
            except ValueError:
                errors.append(f'Prediction row {index} field {score_field} is not an integer.')
                continue

            assert_true(0 <= score <= MAX_SCORE, f'Prediction row {index} field {score_field} is outside 0..{MAX_SCORE}.', errors)


def main():
    errors = []

    validate_aliases(errors)
    validate_results_and_samples(errors)
    validate_app_history_cutoff(errors)
    validate_datasets_and_features(errors)
    validate_predictions(errors)

    if errors:
        print('Validation failed:')
        for error in errors:
            print(f'- {error}')
        raise SystemExit(1)

    print('Validation passed.')


if __name__ == '__main__':
    main()
