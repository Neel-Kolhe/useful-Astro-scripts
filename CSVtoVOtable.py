
#Note from from Neel- requires astropy to run, I used this to plot a
#catalog of RGB stars used in https://www.aanda.org/articles/aa/pdf/2022/04/aa43307-22.pdf  (https://arxiv.org/abs/2204.03662)
#on top of a HI moment 0 map, the catalog was in a csv file, but the visualisation software I used (CARTA https://cartavis.org/)
#only takes VOtable inputs for catalogs

 
from astropy.io import votable
from astropy.io import ascii
# Load CSV data with correct path here
csv_file = 'input_data.csv'

#change according to necessary headers
data_table = ascii.read(csv_file, format='csv', names=['Gra', 'Gdec', 'magv', 'magerr_v', 'mag_i', 'magerr_i'])

# Save  VOtable
VOtable_file = 'yourfilenamehere.vot'
votable.from_table(data_table).to_xml(VOtable_file)
