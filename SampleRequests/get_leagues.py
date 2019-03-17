#sample request
import requests
import json
response = requests.get("https://api-football-v1.p.rapidapi.com/leagues",headers={"X-RapidAPI-Key": "5db1c6e1e7msh416f8b7961cc85ep18b5ffjsn0a06293bea22"})
#make json
data = response.json()
json.dumps(data)
