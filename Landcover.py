#!/usr/bin/env python

# Import numpy

import numpy as np
import pylab as pl

# Import the data

data = np.fromfile("data.bsq",dtype='uint8')

# Split it up

splitdata = np.reshape(data,(21600,43200))

# Checks to see if it did it correctly
#pl.imshow(splitdata[::100,::100])
#pl.show()

# Now we need to have a mapping between some point x,y and a pixel in the map

def point_to_pixel(x, y):
    x = (x + 180)*43200/360
    y = (y + 90)*43200/360 # Fix this!
    return [x,y]

# And now we just check whether this pixel is in water or not

def land_or_water(pixel_point):
    pixel_code = splitdata[pixel_point[0], pixel_point[1]]
    if(pixel_code == 0):
        print "Water"
    else:
        print "Land"

# Put it all together...
    
# Get point - for now, just basic user input
hit_lat = float(raw_input("Enter Latitude: "))
hit_long = float(raw_input("Enter Longitude: "))

# Find which pixel this is 
pixel_hit = point_to_pixel(hit_lat, hit_long)

# And now find out where it hit!
land_or_water(pixel_hit)
