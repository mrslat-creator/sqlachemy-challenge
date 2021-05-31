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
                order_by(Measurement.date).all()
      # Convert List of Tuples Into a Dictionary
      prcp_data_list = dict(prcp_data)
      # Return JSON Representation of Dictionary
      return jsonify(prcp_data_list)

# Station Route
@app.route("/api/v1.0/stations")
def stations():
      # Return a JSON List of Stations From the Dataset
      stations_all = session.query(Station.station, Station.name).all()
      # Convert List of Tuples Into Normal List
      station_list = list(stations_all)
      # Return JSON List of Stations from the Dataset
      return jsonify(station_list)

# TOBs Route
@app.route("/api/v1.0/tobs")
def tobs():
        # Query for the Dates and Temperature Observations from a Year from the Last Data Point
        recent_date = dt.date(2017,8,23)  - dt.timedelta(days=365)
        # Design a Query to Retrieve that Last 12 Months of Preciption Data Selecting Only the 'date' and 'prcp' Values
        tobs_data = session.query(Measurement.date, Measurement.tobs).\
                 filter(Measurement.date >= recent_date).\
                 order_by(Measurement.date).all()
        # Convert List of Tuples Into Normal List
        tobs_data_list = list(tobs_data)
        # Return JSON List of Temperature Observations (tobs) for Previous Year
        return jsonify(tobs_data_list)

# Start Day Route
@app.route("/api/v1.0/<start>")
def start_end_day(start, end):
         start_end_day = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                  filter(Measurement.date >= start).\
                  group_by(Measurement.date).all()
         # Convert List of Tuples Into Normal List
         start_end_day_list = list(start_end_day)
         # Return JSON List of Min Temp, Avy Temp and Max Temp for a Given Start Range
         return jsonify(start_day)_list)

# Start-End Day Route
@app.route("/api/v1.0/<start>/<end>")
def start_end_day(start,end):
        start_end_day = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement)).\
                 filter(Measurement.date >= start).\
                 filter(Measurement.date <= end).\
                 group_by(Measurement.date)all()
        # Convert List of Tuples Into Normal List
        start_end_day_list = list(start_end_day)
        # Return JSON List of Min Temp, Avg Temp and Max Temp for a Given Start-End Range
        return jsonify(start_end_day_list)

# Define Main Behavior
if __name__ == '__main__':
    app.run(debug=True)