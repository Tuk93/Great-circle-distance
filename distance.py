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
        
        #Use The Great Circle distance formula computes the shortest distance path of two points on the surface of the sphere
        
        dist=acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(dlon))
        
        # # Alternately we can use haversine formula to calculate the shortest distance
        #
        # dist = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        # c = 2 * asin(sqrt(h))
        
        r = 6371  # Radius of earth in kilometers. Use 3956 for miles
        
        return r * dist

#create a list to add customers within 100kms range.

customers =[]
#read customer list from json file and calculate the distance from our Dublin office.
for line in open('customer.json', 'r'):
        data = (json.loads(line))
        print(data)
        lat1 = data['latitude']
        print(lat1)

        lon1 = data['longitude']
        print(lon1)
        dub_lat2 = 53.339428
        dub_lon2 = -6.257664

        radius = 100  # in kilometer
        
        obj=Solution()
        a = obj.great_circle(float(lon1), float(lat1), dub_lon2,dub_lat2)

        print('Distance (km) : ', a)
        if a <= radius:
            print('we can invite : ',data['name'])
            customers.append((data['user_id'],data['name']))

        else:
            print('Outside of 100km range from Dublin office')
            
print('total number of customers within 100km range : ',len(customers))

customers=(sorted(customers))
with open('result1.txt', 'w') as filehandle:
     json.dump(customers, filehandle)
#with open('listfile.txt', 'w') as filehandle:
    #filehandle.writelines("%s," % place for place in customers)
