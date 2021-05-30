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
