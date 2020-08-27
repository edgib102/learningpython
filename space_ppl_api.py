import requests

people = requests.get('http://api.open-notify.org/astros.json')
people_json  = people.json()

print("ppl in space:",people_json['number'])
for p in people_json["people"]:
    print(p['name'])
