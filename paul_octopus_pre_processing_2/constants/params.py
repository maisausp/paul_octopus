C_TOURNAMENT = 'FIFA World Cup'

C_TH_GOLS = 8
C_NR_CLASSES = C_TH_GOLS + 1

C_2002_WC = ['2002-05-31', ['Brazil', 'Germany', 'Turkey', 'South Korea', 'Spain', 'England', 'Senegal', 'United States', 'Japan', 'Denmark', 'Mexico', 'Republic of Ireland', 'Sweden', 'Belgium', 'Italy', 'Paraguay', 'South Africa', 'Argentina', 'Costa Rica', 'Cameroon', 'Portugal', 'Russia', 'Croatia', 'Ecuador', 'Poland', 'Uruguay', 'Nigeria', 'France', 'Tunisia', 'Slovenia', 'China PR', 'Saudi Arabia']]
C_2006_WC = ['2006-06-09', ['Italy', 'France', 'Germany', 'Portugal', 'Brazil', 'Argentina', 'England', 'Ukraine', 'Spain', 'Switzerland', 'Netherlands', 'Ecuador', 'Ghana', 'Sweden', 'Mexico', 'Australia', 'South Korea', 'Paraguay', 'Ivory Coast', 'Czech Republic', 'Poland', 'Croatia', 'Angola', 'Tunisia', 'Iran', 'United States', 'Trinidad and Tobago', 'Japan', 'Saudi Arabia', 'Togo', 'Costa Rica', 'Serbia']]
C_2010_WC = ['2010-06-11', ['Spain', 'Netherlands', 'Germany', 'Uruguay', 'Argentina', 'Brazil', 'Ghana', 'Paraguay', 'Japan', 'Chile', 'Portugal', 'United States', 'England', 'Mexico', 'South Korea', 'Slovakia', 'Ivory Coast', 'Slovenia', 'Switzerland', 'South Africa', 'Australia', 'New Zealand', 'Serbia', 'Denmark', 'Greece', 'Italy', 'Nigeria', 'Algeria', 'France', 'Honduras', 'Cameroon', 'North Korea']]
C_2014_WC = ['2014-06-12', ['Germany', 'Argentina', 'Netherlands', 'Brazil', 'Colombia', 'Belgium', 'France', 'Costa Rica', 'Chile', 'Mexico', 'Switzerland', 'Uruguay', 'Greece', 'Algeria', 'United States', 'Nigeria', 'Ecuador', 'Portugal', 'Croatia', 'Bosnia and Herzegovina', 'Ivory Coast', 'Italy', 'Spain', 'Russia', 'Ghana', 'England', 'South Korea', 'Iran', 'Japan', 'Australia', 'Honduras', 'Cameroon']]
C_2018_WC = ['2018-06-14', ['France', 'Croatia', 'Belgium', 'England', 'Uruguay', 'Brazil', 'Sweden', 'Russia', 'Colombia', 'Spain', 'Denmark', 'Mexico', 'Portugal', 'Switzerland', 'Japan', 'Argentina', 'Senegal', 'Iran', 'South Korea', 'Peru', 'Nigeria', 'Serbia', 'Germany', 'Tunisia', 'Poland', 'Saudi Arabia', 'Morocco', 'Australia', 'Iceland', 'Costa Rica', 'Egypt', 'Panama']]
C_2022_WC = ['2022-11-20', ['Australia', 'Iran', 'Japan', 'Qatar', 'Saudi Arabia', 'South Korea', 'Cameroon', 'Ghana', 'Morocco', 'Senegal', 'Tunisia', 'Canada', 'Costa Rica', 'Mexico', 'United States', 'Argentina', 'Brazil', 'Uruguay', 'Belgium', 'Croatia', 'Denmark', 'England', 'France', 'Germany', 'Netherlands', 'Poland', 'Portugal', 'Serbia', 'Spain', 'Switzerland', 'Wales', 'Ecuador']]
C_2026_WC_GROUPS = {
    'A': ['Mexico', 'South Africa', 'South Korea', 'Czech Republic'],
    'B': ['Canada', 'Bosnia and Herzegovina', 'Qatar', 'Switzerland'],
    'C': ['Brazil', 'Morocco', 'Haiti', 'Scotland'],
    'D': ['United States', 'Paraguay', 'Australia', 'Turkey'],
    'E': ['Germany', 'Cura\u00e7ao', 'Ivory Coast', 'Ecuador'],
    'F': ['Netherlands', 'Japan', 'Sweden', 'Tunisia'],
    'G': ['Belgium', 'Egypt', 'Iran', 'New Zealand'],
    'H': ['Spain', 'Cape Verde', 'Saudi Arabia', 'Uruguay'],
    'I': ['France', 'Senegal', 'Iraq', 'Norway'],
    'J': ['Argentina', 'Algeria', 'Austria', 'Jordan'],
    'K': ['Portugal', 'DR Congo', 'Uzbekistan', 'Colombia'],
    'L': ['England', 'Croatia', 'Ghana', 'Panama'],
}
C_2026_WC = ['2026-06-11', [team for group in C_2026_WC_GROUPS.values() for team in group]]

# Features extracted
C_EXTRACT_NR_EMPATES = True # feature idx 3
C_EXTRACT_NR_VICTORIES = True  # feature idx 4
C_EXTRACT_NR_LOSES = True  # feature idx 5

# Type Features extracted
C_EXTRACT_AVERAGE = True

# Period extracted
C_EXTRACT_JUST_PARTICIPANTS = True
C_EXTRACT_32_or_1_year = True
C_EXTRACT_YEARS = 4
