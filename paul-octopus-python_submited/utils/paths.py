import os
from pathlib import Path


APP_DIR = Path(__file__).resolve().parents[1]
PROJECT_DIR = APP_DIR.parent
DEFAULT_2026_DIR = PROJECT_DIR / 'paul-octopus-2026'


def get_data_dir():
    configured_path = os.environ.get('PAUL_OCTOPUS_DATA_DIR')

    if configured_path:
        return Path(configured_path)

    if DEFAULT_2026_DIR.exists():
        return DEFAULT_2026_DIR

    return APP_DIR


def get_data_file(file_name):
    data_file = get_data_dir() / file_name

    if data_file.exists():
        return data_file

    return APP_DIR / file_name


def get_model_file():
    configured_path = os.environ.get('PAUL_OCTOPUS_MODEL_PATH')

    if configured_path:
        return Path(configured_path)

    model_file = get_data_dir() / 'model' / 'MLPClassifier.h5'

    if model_file.exists():
        return model_file

    app_model_file = APP_DIR / 'model' / 'MLPClassifier.h5'

    if app_model_file.exists():
        return app_model_file

    return APP_DIR / 'MLPClassifier.h5'
