def get_population(country_data):
  population_dict = {
    '2022': int(country_data['2022 Population']),
    '2020': int(country_data['2020 Population']),
    '2015': int(country_data['2015 Population']),
    '2010': int(country_data['2010 Population']),
    '2000': int(country_data['2000 Population']),
    '1990': int(country_data['1990 Population']),
    '1980': int(country_data['1980 Population']),
    '1970': int(country_data['1970 Population'])
  }
  labels = population_dict.keys()
  values = population_dict.values()
  return labels , values
  
def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country, data))
  return result 

def get_world_percentages(data):
  percentages = list(map(lambda item: item['World Population Percentage'], data))
  return percentages

def get_country(data):
  countries = list(map(lambda item: item['Country/Territory'], data))
  return countries