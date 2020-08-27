import requests

print("What do you wnat to find out what rhymes with")
parameter = {"rel_rhy":input()}
request = requests.get('https://api.datamuse.com/words',parameter)

rhyme_json = request.json()
print(rhyme_json)
print("how many word do you wan to see?")
num = int(input())
for i in rhyme_json[0:num]:
  print(i['word'])