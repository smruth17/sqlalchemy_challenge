from flask import Flask, jsonify
import pandas as pd
import numpy as np
from sqlHelper import SQLHelper

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
sql = SQLHelper()

#################################################
# Flask Routes
#################################################
      
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

#####QUERIES#####
@app.route("/api/v1.0/precipitation")
def precipitation():
	data = sql.query_precipitation()
	return(jsonify(data))

@app.route("/api/v1.0/stations")
def stations():
	data = sql.query_stations()
	return(jsonify(data))

@app.route("/api/v1.0/tobs")
def tobs():
	data = sql.query_tobs()
	return(jsonify(data))

@app.route("/api/v1.0/<start>")
def <start>():
	data = sql.query_<start>()
	return(jsonify(data))


# Run the App
if __name__ == '__main__':
    app.run(debug=True)


# Returns Json with the date as the key and the value as precipitation
# Only returns the jsonified precipitation data for the last year in the database


    