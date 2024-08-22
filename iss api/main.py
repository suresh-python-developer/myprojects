import requests
from datetime import datetime
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()
# print(data)
# lattitude = data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]
#
# iss_position =(lattitude,longitude)
# print(iss_position)
parameters = {
    "lat" :10.363260,
    "lng": 77.982491

}
response = requests.get(url=" https://api.sunrise-sunset.org/json?lat=10.363260&lng= 77.982491&formatted=0")
sunrise = response.json()["results"]["sunrise"]
sunset = response.json()["results"]["sunset"]
print(sunrise.split("T")[1].split(":")[0])
print(sunset.split("T")[1].split(":")[0])

time_now = datetime.now()
print(time_now.hour)