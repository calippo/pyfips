import pandas
import sys, os
dataLocation = os.getcwd() + '/data/'

def getLatLon(fips):
  df = pandas.read_csv(dataLocation + 'locations.csv', index_col=False, header=0);
  fipsToCoordinates = dict(zip(df['fips'],zip(df['lat'],df['lng'])))
  return fipsToCoordinates[fips]

def getSateLatLon(fips):
  state = fipToState(fips)
  df = pandas.read_csv(dataLocation + 'locations.csv', index_col=False, header=0);
  fipsToCoordinates = df[['state','lat', 'lng']]
  stateData = fipsToCoordinates[fipsToCoordinates['state'] == state]
  lat = stateData['lat'].sum()/len(stateData)
  lon = stateData['lng'].sum()/len(stateData)
  return (lat, lon)

def fipToState(fips):
  df = pandas.read_csv(dataLocation + 'state_table.csv', index_col=False, header=0);
  code = int(fips[0:2])
  state = df[['fips_state','abbreviation']]
  abbreviation = state[state['fips_state'] == code]['abbreviation'].irow(0)
  return abbreviation

if __name__ == '__main__':
  print getSateLatLon(str(sys.argv[1]))