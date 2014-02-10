import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pyfips",
    version = "0.2",
    author = "Claudio Caletti",
    author_email = "caletti.claudio@gmail.com",
    description = ("convert fips to latitude and longitude"),
    license = "BSD",
    keywords = "fips geospatial"
)