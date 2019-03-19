import pandas as pd

# pd.set_option('display.max_colwidth', 10000)
# pd.options.display.max_colwidth = 1000
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])

population = pd.Series([852469, 1015785, 485199])

cities = pd.DataFrame({'City name': city_names, 'Population': population})

cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
cities['Population density'] = cities['Population'] / cities['Area square miles']

# print(cities['Area square miles'] > 50)

cities['Is wide and has saint name'] = (cities['Area square miles'] > 50) & \
                                       (cities['City name'].apply(lambda name: name.startswith('San')))

print(cities.iloc[0])

cities = cities.reindex([0, 1, 2, 3])

print(cities)

# california_housing_dataframe = pd.read_csv(
#     "https://download.mlcc.google.cn/mledu-datasets/california_housing_train.csv", sep=",")
# print(california_housing_dataframe.describe(include='all'))
