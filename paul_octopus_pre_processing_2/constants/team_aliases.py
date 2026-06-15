TEAM_ALIASES = {
    'Cabo Verde': 'Cape Verde',
    'Cape Verde Islands': 'Cape Verde',
    'China': 'China PR',
    'China PR': 'China PR',
    'Curacao': 'Cura\u00e7ao',
    'Czechia': 'Czech Republic',
    'Czech Republic': 'Czech Republic',
    'Democratic Republic of the Congo': 'DR Congo',
    'DRC': 'DR Congo',
    'Korea Republic': 'South Korea',
    'South Korea': 'South Korea',
    'Turkiye': 'Turkey',
    'Turkey': 'Turkey',
    'USA': 'United States',
    'US': 'United States',
    'United States': 'United States',
    "Cote d'Ivoire": 'Ivory Coast',
    "C\u00f4te d'Ivoire": 'Ivory Coast',
}


def normalize_team_name(team_name):
    return TEAM_ALIASES.get(team_name, team_name)


def normalize_team_names(team_names):
    return [normalize_team_name(team_name) for team_name in team_names]
