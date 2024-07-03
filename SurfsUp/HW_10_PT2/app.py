import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify

# Database Setup
engine = create_engine("sqlite:///hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)
# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Flask Setup
app = Flask(__name__)

# Flask Routes
@app.route("/")
def home():
	return (
	f"Available Routes:<br/>"
	f"/api/v1.0/precipitation<br/>" 
	f"/api/v1.0/stations<br/>"
	f"/api/v1.0/tobs<br/>"    
	f"/api/v1.0/<start><br/>"
	f"/api/v1.0/<start>/<end><br/>"
	)

# QUERIES

# Returns Json with the date as the key and the value as precipitation
# Only returns the jsonified precipitation data for the last year in the database

@app.route("/api/v1.0/precipitation")
def precipitation():

	session = Session(engine)

	# Calculate the date one year from the last date in data set.
	begin_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)

	# Perform a query to retrieve the data and precipitation scores
	results = session.query(Measurement.date, Measurement.prcp)\
		.filter(Measurement.date >= begin_date)\
		.group_by(Measurement.date)\
		.all()
	
	session.close()

	precipitation_data = {}
	for date, prcp in results:
		precipitation_data[date] = prcp

	return jsonify(precipitation_data)


# Returns jsonified data of all of the stations in the database

@app.route("/api/v1.0/stations")
def stations():
	session = Session(engine)
	results = session.query(Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation).all()

	session.close()

	station_data = []
	for station, name, latitude, longitude, elevation in results:
		station_dict = {}
		station_dict["name"] = name
		station_dict["latitude"] = latitude
		station_dict["longitude"] = longitude
		station_dict["elevation"] = elevation
		station_data.append(station_dict)

	return jsonify(station_data)

# Returns jsonified data for the most active station (USC00519281)
# Only returns the jsonified data for the last year of data 

@app.route("/api/v1.0/tobs")
def tobs():
	session = Session(engine)

	most_active = "USC00519281"
	begin_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
	results = session.query(Measurement.station, Measurement.date, Measurement.prcp, Measurement.tobs) \
		.filter(Measurement.station == most_active) \
		.filter(Measurement.date >= begin_date) \
		.all()

	
	tobs_data = []
	for result in results:
		tobs_data.append({
			"station": result[0],
			"date": result[1],
			"prcp": result[2],
			"tobs": result[3]
		})
		return(jsonify(tobs_data))

# Accepts the start date as a parameter from the URL 
# Returns the min, max, and average temperatures calculated from the given start date to the end of the dataset
# @app.route("/api/v1.0/<start>")
# def <start>():
# session = Session(engine)

# 	return(jsonify(data))

# Accepts the start and end dates as parameters from the URL 
# Returns the min, max, and average temperatures calculated from the given start date to the given end date 
# @app.route("/api/v1.0/<start>")
# def <start>():
# 	session = Session(engine)

# 	return(jsonify(data))

# Run the App
if __name__ == '__main__':
	app.run(debug=True)


    