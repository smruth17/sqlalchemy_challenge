
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text, func

import pandas as pd
import numpy as np
import datetime as dt

class SQLHelper():
    #################################################
    # Database Setup
    #################################################

# define properties
    def __init__(self):
        self.engine = create_engine("sqlite:///hawaii.sqlite")
        self.Base = None

        # automap Base classes
        self.init_base()

    def init_base(self):
        # reflect an existing database into a new model
        self.Base = automap_base()
        # reflect the tables
        self.Base.prepare(autoload_with=self.engine)

    #################################################
    # Database Queries
    #################################################

    def query_precipitation(self):
        # Save reference to the table
        Measurement = self.Base.classes.measurement

        # Create our session (link) from Python to the DB
        session = Session(self.engine)

        ## Calculate the date one year from the last date in data set.
        begin_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)

        # Perform a query to retrieve the data and precipitation scores
        # Perform a query to retrieve the data and precipitation scores
        results = session.query(Measurement.date, Measurement.prcp)\
            .filter(Measurement.date >= begin_date)\
            .group_by(Measurement.date)\
            .all()

        # close session
        session.close()

        df = pd.DataFrame(results)
        data = df.to_dict(orient="records")
        return(data)
