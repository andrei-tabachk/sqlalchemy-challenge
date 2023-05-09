# Import the dependencies.
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
import numpy as np
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################
app = Flask(__name__)
#################################################
# Flask Routes
#################################################

@app.route ("/")
def welcome():
    return (
        f"Welcome to the Andrei's Surfs Up API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/insert(yyyy-mm-dd)<start><br/>"
        f"/api/v1.0/insert(yyyy-mm-dd)<start>/(yyyy-mm-dd)<end>"
    )

@app.route ("/api/v1.0/percipitation")
def percipitation():
    session = Session(engine)
    results_perc = session.query(measurement.date,measurement.prcp).\
                        filter(measurement.date >= '2016-08-23').\
                        order_by(measurement.date).all()
    session.close()

    all_perc = []
    for date, prcp in results_percipitation:
        percip_dict = {}
        percip_dict["date"] = date
        percip_dict["prcp"] = prcp
        all_perc.append(precip_dict)

    return jsonify(all_perc)

@app.route ("/api/v1.0/stations")
def stations():
    session = Session(engine)
    
    station_results = session.query(station.station).all()

    session.close()

    all_station = list(np.ravel(station_results))

    return jsonify(all_station)

