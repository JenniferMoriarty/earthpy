
from glob import glob

import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep

import rasterio as rio

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

import plotly.graph_objects as go

np.seterr(divide='ignore', invalid='ignore')

S_sentinel_bands = glob("sundarbans_data/*B?*.tiff")

S_sentinel_bands.sort()
print(S_sentinel_bands)


l = []

for i in S_sentinel_bands:
  with rio.open(i, 'r') as f:
    l.append(f.read(1))
    print("pushed band into list!")
    
arr_st = np.stack(l)

ep.plot_bands(arr_st, 
              cmap = 'gist_earth', 
              figsize = (10, 5), 
              cols = 6, 
              cbar = False)
plt.show()

# RGB Composite Image

rgb = ep.plot_rgb(arr_st, 
                  rgb=(3,2,1), 
                  figsize=(10, 16))
plt.show()

rgb = ep.plot_rgb(arr_st, 
                  rgb=(3,2,1), 
                  figsize=(10, 16))
plt.show()

# RGB Composite Image with Strech

#ep.plot_rgb(arr_st,
#            rgb=(3, 2, 1),
#            stretch=True,
#            str_clip=0.2,
#            figsize=(10, 16))
#plt.show()