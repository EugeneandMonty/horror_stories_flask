import json
import glob

data = json.load(open('test-data.json'))

list = glob.glob("/Users/kate/Documents/GitHub/horror_stories_react/public/images/*")
listready = []

for each in list:
    mod_data = each.replace('/Users/kate/Documents/GitHub/horror_stories_react/public/', '')
    listready.append(mod_data)

  