import requests
from datetime import datetime
import smtplib

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
EMAIL_ID = 'elango9585336785@gmail.com'
PASSWORD = 'qxchdrlsgrypnhgt'


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour = time_now.hour
if hour > 12:
    hour -= 12

response_iss = requests.get('http://api.open-notify.org/iss-now.json')
response_iss.raise_for_status()
data_iss = response_iss.json()


if MY_LONG - 5 <= float(data_iss['iss_position']['longitude']) <= MY_LONG + 5 and MY_LAT - 5 <= float(data_iss['iss_position'][
    'latitude']) <= MY_LAT + 5 and sunset <= hour <= sunrise:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=EMAIL_ID,password=PASSWORD)
        connection.sendmail(from_addr=EMAIL_ID,to_addrs=EMAIL_ID,msg=f'Subject: ISS is Right above your head')

#If the ISS is close to my current position

# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



