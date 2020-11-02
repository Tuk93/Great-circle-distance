
from math import radians, degrees, sin, cos, asin, acos, sqrt
import json

class Solution:
    def __init__(self):
        self.lon2 = 53.339428
        self.lat2 = -6.257664

    def great_circle(self,lon1, lat1, lon2, lat2):
        # type: (object, object, object) -> object
        """
        Calculate the great circle distance between two points
        on the earth (specified in decimal degrees)
        """
        # convert decimal degrees to radians
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        
        #calculate the difference between 2 longitudes
        dlon = lon2 - lon1 
        dlat = lat2 - lat1
        
        #Use The Great Circle distance formula to compute the shortest distance path of two points on the surface of the sphere
        
        dist=acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(dlon))
        
        # # Alternately we can use haversine formula to calculate the shortest distance
        #
        # dist = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        # c = 2 * asin(sqrt(h))
        
        r = 6371  # Radius of earth in kilometers. Use 3956 for miles
        
        return r * dist

#create a list to add customers within 100kms range.

