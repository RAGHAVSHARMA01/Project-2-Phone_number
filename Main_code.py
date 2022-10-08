import phonenumbers
import folium
# now let's import the phone number from the different file we created and using the code below we can call that into this main file and this code will give us the country the phone number belong to
from numbers_to_check import number

from phonenumbers import geocoder

Key = '8c647d47cf384647b961f14e4353c95e'  # Key that is generated from the opencagedata.com by making a account on it

samNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(samNumber, "en")
print(yourLocation)

# Now we wil aim to get the Service provider of that number

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "eng"))

# Lets get the latitude and the logitude to make a location on map

from  opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(Key)

query = str(yourLocation)

results = geocoder.geocode(query)
# print(results)   ## TO PRINT WHOLE DATA WITH LAT AND LNG

# TO ONLY PRINT THE LAT AND LNG
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

myMap = folium.Map(location=[lat,lng], zoom_start = 9)


# making a marker
folium.Marker([lat,lng], popup=yourLocation).add_to(myMap)

# save map in html file
myMap.save("mylocation.html")


