


cities= ["NY", "Moscow", "new dehli", "Minsk", "Toronto"]
print(cities)
print(len(cities))

print(cities[-1])
print(cities[2].title())

cities[2] = 'Tula'
print(cities)

cities.append("Riga")
print(cities)

cities.insert(2, 'Feodosia')
print(cities)

del cities[-1]
print(cities)


cities.remove("Tula")
print(cities)

deleted_city = cities.pop()
print("deleted ity is:" + deleted_city)

cities.sort()

cities.sort(reverse=True)
print(cities)

cities.reverse()
print(cities)

