Monitor
=======

It's mainly a toy to discover influxdb

Setup
-----

This is my personal setup, used for current development.

The flask app is running on an openbsd box and python 3.6 alongside a
influxdb. A sensor running on a wemos d1 mini pro post every second the
temperature and humidity.

The influxdb will store a mean of the incoming data every minutes and
ten minutes, only keep the raw values for 2h, the 60s average for 4
weeks and the 10 minutes average for 52 weeks.

Running
-------

Nothing fancy.

```
$ python3 -m venv env
$ pip install -r requirements.txt
$ FLASK_APP=app.py flask run --host=0.0.0.0 --debugger --reload
```

This will create a virtual environment for python3, install flask and
the influxdb client and run the app in a development mode accessible by
other machines on the network.
