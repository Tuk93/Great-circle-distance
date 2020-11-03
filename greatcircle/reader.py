from distance import *

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
with open('output.txt', 'w') as filehandle:
     json.dump(customers, filehandle)
