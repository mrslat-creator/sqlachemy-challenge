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


# Database Setup

#