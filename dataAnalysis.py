import csv
from os import PathLike
import plotly.express as px

rows = []
with open("cleanedData.csv", "r") as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        rows.append(row)
headers = rows[0]
planetData = rows[1:]
# print(headers)
# print(planetData)
headers[0] = "row_num"
solarSystemPlanetCount = {}
for planet_data in planetData:
    if solarSystemPlanetCount.get(planet_data[11]):
        solarSystemPlanetCount[planet_data[11]] += 1
    else:
        solarSystemPlanetCount[planet_data[11]] = 1
maxSolarSystem = max(solarSystemPlanetCount, key = solarSystemPlanetCount.get)
# print(solarSystemPlanetCount[maxSolarSystem])
# print(maxSolarSystem)
tempPlanetRows = list(planetData)
for planet_data in tempPlanetRows:
    planetMass = planet_data[3]
    if planetMass.lower() == "unknown":
        planetData.remove(planet_data)
        continue
    else:
        planetMassValue = planetMass.split(" ")[0]
        planetMassRef = planetMass.split(" ")[1]
        if planetMassRef == "Jupiters":
            planetMassValue = float(planetMassValue)*317.8
        planet_data[3] = planetMassValue
    planetRadius = planet_data[7]
    if planetRadius.lower() == "unknown":
        planetData.remove(planet_data)
        continue
    else:
        planetRadiusValue = planetRadius.split(" ")[0]
        planetRadiusRef = planetRadius.split(" ")[2]
        if planetRadiusRef == "Jupiter":
            planetRadiusValue = float(planetRadiusValue)*11.2
        planet_data[7] = planetRadiusValue
# print(len(planet_data))
# print(len(planetData))
newPlanet = []
for planet_data in planetData:
    if maxSolarSystem == planet_data[11]:
        newPlanet.append(planet_data)
# print(newPlanet)
# print(len(newPlanet))
KOI_planet_mass = []
KOI_planet_name = []
KOI_planet_radius = []
for planet_data in newPlanet:
    KOI_planet_mass.append(planet_data[3])
    KOI_planet_name.append(planet_data[1])
    KOI_planet_radius.append(planet_data[7])
KOI_planet_mass.append(1)
KOI_planet_name.append("Earth")
KOI_planet_radius.append(6371)
# fig = px.bar(x = KOI_planet_name, y = KOI_planet_mass)
# fig.show()
KOI_planet_gravity = []
for index, name in enumerate(KOI_planet_name):
    gravity = ((float(KOI_planet_mass[index])*5.972e+24) / ((float(KOI_planet_radius[index])*float(KOI_planet_radius[index]))*6371000*6371000))*6.67408e-11
    # gravity = (float(KOI_planet_mass[index])*5.972e+24) / (float(KOI_planet_radius[index])*float(KOI_planet_radius[index])*6371000*6371000) * 6.67408e-11
    KOI_planet_gravity.append(gravity)
    # print(KOI_planet_name[index])
    # print(KOI_planet_mass[index])
    # print(KOI_planet_radius[index])
# print(KOI_planet_gravity)
fig2 = px.scatter(x = KOI_planet_radius, y = KOI_planet_mass, size = KOI_planet_gravity, hover_data = [KOI_planet_name])
# fig2.show()
low_gravity_planets = []
for index, gravity in enumerate(KOI_planet_gravity):
    if gravity < 10:
        low_gravity_planets.append(planetData[index])
# print(len(low_gravity_planets))
planet_type = []
for planet_data in planetData:
    planet_type.append(planet_data[6])
# print(list(set(planet_type)))

# ---------------------------------------------------------------------------------------------------------

temp_planet_rows = list(planetData)
for planet_data in temp_planet_rows:
    if planet_data[1].lower() == "KOI-351":
        planetData.remove(planet_data)
# print(temp_planet_rows)

temp_planet_mass = []
temp_planet_name = []
temp_planet_radius = []
temp_planet_type = []
temp_planet_gravity=[]
for planet_data in planetData:
    temp_planet_mass.append(planet_data[3])
    temp_planet_name.append(planet_data[1])
    temp_planet_radius.append(planet_data[7])
    temp_planet_type.append(planet_data[6])
temp_planet_mass.append(1)
temp_planet_name.append("Earth")
temp_planet_radius.append(1)
temp_planet_type.append("Terrestrial")
temp_planet_gravity.append(9.80665)
# fig3 = px.bar(x = temp_planet_name, y = temp_planet_mass)
# fig3.show()
for index, name in enumerate(temp_planet_name):
    gravity = ((float(temp_planet_mass[index])*5.972e+24) / ((float(temp_planet_radius[index])*float(temp_planet_radius[index]))*6371000*6371000))*6.67408e-11
    temp_planet_gravity.append(gravity)
# fig4 = px.scatter(x = temp_planet_radius, y = temp_planet_mass, size = temp_planet_gravity, hover_data = [temp_planet_type, temp_planet_name])
# fig4.show()
temp_low_gravity_planets = []
for index, gravity in enumerate(temp_planet_gravity):
    if gravity < 10:
        temp_low_gravity_planets.append(planetData[index-1])
print(len(temp_planet_gravity))
print(len(temp_low_gravity_planets))