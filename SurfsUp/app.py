# Import the dependencies.
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import datetime as dt
import numpy as np

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

# reflect an existing database into a new model
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = FLask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
        """List all available api routes."""
        return (
                f"Available Routes:<br/>"
                f"api/v1.0/precipitation<br/>"
                f"api/v1.0/stations<br/>"
                f"api/v1.0/tobs<br/>"
                f"api/v1.0/<start><br/>"
                f"api/v1.0/<start>/<end><br/>"
        )

@app.route("api/v1.0/precipitation")
def  precipitation():
        

@app.route("api/v1.0/stations")
def  stations():
        

@app.route("api/v1.0/tobs")
def  tobs():
        

@app.route("api/v1.0/<start>")
def  <start>():
        

@app.route("api/v1.0/<start>/<end>")
def  <start>/<end>():
        
