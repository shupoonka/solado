import json

with open('config_toy.json') as config_file:
    data = json.load(config_file)

app = data['app']
name = app['name']

print(app)
print(name)