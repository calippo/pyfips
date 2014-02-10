import os
from setuptools import setup

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
