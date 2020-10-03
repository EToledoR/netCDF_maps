from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap


nc = '/home/eduardo/Projects/Thesis/data/EA_m30_meantime.nc'
fh = Dataset(nc, mode='r')

lat = fh.variables['lat'][:]
lon = fh.variables['lon'][:]
time = fh.variables['time'][:]
totp = fh.variables['totp'][:] # Total precipitations

totp_units = fh.variables['totp'].units

fh.close()

map = Basemap(projection='merc',llcrnrlon=20.,llcrnrlat=-20.,urcrnrlon=60.,urcrnrlat=30.,resolution='i')

map.drawcoastlines()
map.drawcountries()
map.drawlsmask(land_color='Linen', ocean_color='#CCFFFF') # can use HTML names or codes for colors

parallels = np.arange(-20,30,5.) # make latitude lines ever 5 degrees from 30N-20S
meridians = np.arange(20,60,5.) # make longitude lines every 5 degrees from 20E to 60E
map.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)
map.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)

lons,lats= np.meshgrid(lon,lat)
x,y = map(lons,lats)

cs = map.pcolor(x,y,np.squeeze(totp))

cbar = map.colorbar(cs, location='bottom', pad="10%")
cbar.set_label(totp_units)

plt.title('Total Precipitations mean per year')

plt.show()
#plt.savefig('totp.png')

