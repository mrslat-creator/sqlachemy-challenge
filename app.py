# Import Flask
from flask import Flask, jsonify

# Dependencies and Setup
import numpy as np
import datetime as dt

# Python SQL Toolkit and Object Relational Mapper
import squlalchemy
from sqalchemy.ext.automap import automap_base
from sqalchemy.orm import Session
from sqalchemy import create_engine, func
from sqalchemy.pool import StaticPool

#####################################
# Database Setup
#####################################
# Reference
engine = create_engine("sqlite:///Resources/hawaii.sqlite", connect_args={"check_same_thread": False}, poolclass=StaticPool, echo=True)

# Reflect Existing Database Into a New Model
Base = automap_base()
# Reflect the Tables
Base.prepare(engine, reflect=True)

# Save Refrences to Each Table
Measurement = Base.classes.measurement
Station =Base.classes.station

# Create session (link) from Python to the DB
session = Session(engine)

###################################
# Flask Setup
###################################
app = Flask(_name_)

###################################
# Flask Route
###################################
# Home Route
@app.route("/")
def welcome():
       return"""<html>
<h1>Hawaii Climate App (Flask API)</h1>
<img src="https://i.ytimg.com/vi3ZMvhIO-d4/maxresdefault.jpg" alt="Hawaii Weather"/>
<p>Precipation Analysis:</p>
<ul>
  <li><a href="/api/v1.0/precipitation">/api/v1.0/percipitation</a></li>
</ul>
<p>Station Anaylsis:</p>
<ul>
  <li.<a href="/api/v1.0/stations">/api/v1.0/stations</a><li>
</ul>
<p>Temperature Analysis:<p/>
<ul>
   <li><a href="/api/v1.0/tobs">/api/v1.0/tobs</a></li>
</ul>
<p>Start Day Analysis:</p>
<ul>
   <li><a href="/api/v1.0/2017-03-14">/api/v1.0/2017-03-14</a></li>
<ul>
<p>Start & End Day Analysis:</p>
<ul>
   <li><a href="/api/v1.0/2017-03-14/2017-03-28">/api/v1.0/2017-03-14/2017-03-28</a></li>
</ul>
</html>
"""

# Precipitation Route
@app.route("/api/v1.0/precipitation")
def precipitation():
      # Convert the Qurery Results to a Dictionary Using 'date' as the Key and 'prcp' as the Value
      # Calculate the Date 1 Year Ago from the Last Data Point in the Datanase
      recent_date = dt.date(2017,8,23) - dt.timedelta(days=365)
      # Design a Query to Retrive the Last 12 Months of Precipitation Data Selecting Only the 'date' and 'prcp' Values
      prcp_data = session.query(Measurement.date, Measurement.prcp).\
                filter(Measurement.date >= one_year_ago).\
                order_by(Measurement)