import json
import requests

app_id = "993e59c3"
app_key = "097293b314380ee44daa501cb8bcd5f6"

# 'entries' retrieve meaning of the word & ‘thesaurus’ retrieve similar words & ‘sentences’ retrieve example sentences
endpoint = "entries"
#
language_code = "en-us"
# Here we pass the word
word_id = "example"

url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language_code + "/" + word_id.lower()

r = requests.get(url, headers = {"app_id": app_id, "app_key": app_key})

print("code {}\n".format(r.status_code))
# print("text \n" + r.text)
string_1 = json.dumps(r.json())
dict_1 = json.loads(string_1)
# print(dict_1)
print(dict_1.keys())
print(dict_1["results"])
