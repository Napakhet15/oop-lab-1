import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany
print("All cities in Germany:")
temps = []
for city in cities:
    if city['country'] == 'Germany':
        temps.append(city)
print(temps)
print()

# Print all cities in Spain with a temperature above 12°C
print("All cities in Spain with a temperature above 12°C:")
temps = []
for city in cities:
    if city['country'] == 'Spain' and float(city['temperature']) >12:
        temps.append(city)
print(temps)
print()

# Count the number of unique countries
print("Count the number of unique countries:")
temps = []
for city in cities:
    if city['country'] not in temps:
        temps.append(city['country'])
print(len(temps))
print()

# Print the average temperature for all the cities in Germany
print("The average temperature for all the cities in Germany:")
temps = []
for city in cities:
    if city['country'] == 'Germany':
        temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()


# Print the max temperature for all the cities in Italy
print("The max temperature for all the cities in Italy:")
temps = []
for city in cities:
    if city['country'] == 'Italy':
        temps.append(float(city['temperature']))
print(max(temps))
print()

# Let's write a function to filter out only items that meet the condition
# Hint: condition will be associated with an anonymous function, e.x., lamdbda x: max(x)
def filter(condition, dict_list):
    temps = []
    for item in dict_list:
        if condition(item):
            temps.append(item)
    return temps

# Print all cities in Germany
filtered_list = filter(lambda x: x['country'] == 'Germany', cities)
print(filtered_list)

# Let's write a function to do aggregation given an aggregation function and an aggregation key
def aggregate(aggregation_key, aggregation_function, dict_list):
    data = []
    for item in dict_list:
        x = item[aggregation_key]
        try:
            x = float(x)  
        except ValueError:
            pass
        data.append(x)
    return aggregation_function(data)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
tem = aggregate('temperature',lambda x: sum(x)/len(x),cities)
print(tem)
print()

# Print all cities in Spain with a temperature above 12°C
print("All cities in Spain with a temperature above 12°C")
fil_spain = filter(lambda x: x['country'] == 'Spain' and float(x['temperature']) > 12, cities)
print(fil_spain)
print()

# Count the number of unique countries
print("the number of unique countries")
uniq = aggregate('country',lambda x: len(set(x)), cities)
print(uniq)
print()

# Print the average temperature for all the cities in Germany
print("The average temperature for all the cities in Germany:")
fil_ger = filter(lambda x: x['country'] == 'Germany', cities) 
ave_ger = aggregate('temperature',lambda x: sum(x)/ len(x), fil_ger)
print(ave_ger)
print()

# Print the max temperature for all the cities in Italy
print("The max temperature for all the cities in Italy:")
fil_it = filter(lambda x: x['country'] == 'Italy', cities) 
max_it = aggregate('temperature',lambda x: max(x), fil_it)
print(max_it)
print()