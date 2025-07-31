from astropy.utils.data import download_file
from astropy.io import fits


# Downloads the HI data in a fits file format
cube_url=    "http://data.astropy.org/tutorials/FITS-cubes/reduced_TAN_C14.fits"

filename = download_file(cube_url, cache=True, show_progress=True)

hdul = fits.open(filename)
hdul.info()

import matplotlib.pyplot as plt
import numpy as np

data = hdul[0].data  # forma: (velocità, y, x)
header = hdul[0].header

print("Shape del datacube:", data.shape)

# Estrai uno slice 2D (es. piano a velocità Z = 50)
slice_index = 50
image = data[slice_index, :, :]

# Mostra lo slice
plt.imshow(image, origin='lower', cmap='plasma')
plt.colorbar(label='Intensità HI')
plt.title(f'Slice del datacube (Velocità index = {slice_index})')
plt.show()


# Coordinate pixel: (y, x)
y, x = 100, 150
spectrum = data[:, y, x]

plt.plot(spectrum)
plt.xlabel('Canale di velocità')
plt.ylabel('Intensità HI')
plt.title(f'Spettro al pixel ({x}, {y})')
plt.grid(True)
plt.show()
# Chiudi il file FITS
hdul.close()