import logging

from flask import Flask
from flask import abort, render_template, request
from influxdb import InfluxDBClient

log = logging.getLogger(__name__)
app = Flask(__name__)
client = InfluxDBClient(database='monitor')

app.config['TEMPLATES_AUTO_RELOAD'] = True

env_for_place = """
    SELECT "temperature", "humidity"
    FROM "monitor"."a_month"."environment"
    WHERE "place" = '%(place)s'
        AND now() - 6h < time
"""


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<string:place>/')
def show_environment(place):
    result = client.query(env_for_place % {'place':place})
    ctx = {
        'place': place,
        'environment': result.get_points(),
    }
    return render_template("environment.html", **ctx)


@app.route('/<string:place>/post/', methods=['POST'])
def add_environment(place):
    data = [{
        "measurement": "environment",
        "tags": {
            "place": place,
        },
        "fields": {
            'temperature': float(request.form['temperature']),
            'humidity': float(request.form['humidity']),
        },
    }]
    success = client.write_points(data)
    if not success:
        abort(400)
    return 'ok.'

