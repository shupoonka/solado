from flask import Flask, escape, request
import json

with open('config_toy.json') as config_file:
    data = json.load(config_file)

app = data['app']
name = app['name']

print(app)
print(name)

app = Flask(__name__)


@app.route('/')
def hello():
    name1 = request.args.get("name", "World")
    return f'Hello, {escape(name1)}!'


if __name__ == '__main__':
    app.run()