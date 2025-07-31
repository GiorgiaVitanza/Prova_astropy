from astropy.utils.data import download_file
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

# Scarica il file
file = download_file("http://data.astropy.org/tutorials/FITS-images/HorseHead.fits", cache=True)

# Apri il file FITS
hdul = fits.open(file)
hdul.info()
data0 =hdul[0].data
header = hdul[0].header         

# === 2. Controlla i metadati ===
print("Informazioni FITS:")
print(repr(header))

# === 3. Preprocessing: rimuovi NaN, normalizza ===
data = np.nan_to_num(data0) # Sostituisce NaN con 0
data = data - np.min(data)  # Shift verso 0
data = data / np.max(data)  # Normalizzazione [0,1]

# === 4. Maschera outlier estremi (opzionale) ===
threshold = 0.98
data[data > threshold] = threshold

# === 5. Visualizza l'immagine ===
plt.imshow(data, cmap='gray', origin='lower')
plt.colorbar(label='Intensità normalizzata')
plt.title('Immagine FITS Normalizzata')


# === 5. Visualizza l'immagine ===
plt.imshow(data0,cmap='gray', origin='lower')
plt.colorbar(label='Intensità normalizzata')
plt.title('Immagine FITS non normalizzata   ')
plt.show()

# === 6. Chiudi il file FITS ===
hdul.close()
