import json
import behave2cucumber
with open('features/fajl9999.json') as behave_json:
    cucumber_json = behave2cucumber.convert(json.load(behave_json))
    print(cucumber_json)