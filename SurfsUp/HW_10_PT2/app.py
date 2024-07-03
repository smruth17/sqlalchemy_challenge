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

# Run the App
if __name__ == '__main__':
	app.run(debug=True)




# @app.route("/api/v1.0/stations")
# def stations():
# 	data = sql.query_stations()
# 	return(jsonify(data))

# @app.route("/api/v1.0/tobs")
# def tobs():
# 	data = sql.query_tobs()
# 	return(jsonify(data))

# @app.route("/api/v1.0/<start>")
# def <start>():
# 	data = sql.query_<start>()
# 	return(jsonify(data))








    