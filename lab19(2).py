import pickle

population_data = {
    'Германия': 83166711,
    'Франция': 67081000,
    'Италия': 60244639,
    'Испания': 47450795,
    'Украина': 41732779,
    'Польша': 38386000,
    'Румыния': 19286123,
    'Нидерланды': 17441139,
    'Греция': 10724599,
    'Чехия': 10701777,
    'Португалия': 10305564,
    'Швеция': 10327589,
    'Венгрия': 9769526,
    'Австрия': 8917205
}

average_population = sum(population_data.values()) / len(population_data)

selected_countries = {country: pop for country, pop in population_data.items() if pop > average_population}

with open('country.dat', 'wb') as f:
    pickle.dump(selected_countries, f)

print('Дані записані в файл country.dat')

import pickle

with open('country.dat', 'rb') as f:
    selected_countries = pickle.load(f)

print('Країни з населенням більше середьного:')
print(selected_countries)
