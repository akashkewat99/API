import requests
import json

def data():
  while(True):  
    tem=input("Enter City Name: ").title()
    web="https://api.openweathermap.org/data/2.5/weather?q={}&APPID=f22f2808280c2f36089d55e881ac875b".format(tem)
    response = requests.get(web)
    v=(response.status_code)
    if v==200:
      obj = response.json()  ##converting into dict
      # print(type(obj)) ####### Now its Dic
      # x=obj["main"]
      # print(x["temp"])
      x=(round((obj["main"]["temp"]-273.15)))
      x=(u'{}\N{DEGREE SIGN}'.format(x))
      print("The Temperature in "+tem+" is {}C".format(x))
      return
    elif v==404:
      print("Please enter correct city name")
data()