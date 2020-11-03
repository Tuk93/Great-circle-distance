from dynamodb import *

for line in open('customer.json', 'r'):
        data = (json.loads(line))
        print(data)
        lat1 = data['latitude']
        print(lat1)

        lon1 = data['longitude']
        print(lon1)
        

       	PutItemInput = {
            'Item': {
                'user_id': {'N':str(data['user_id'])},
                'name': {'S': data['name']}

            }

	}
	geoDataManager.put_Point(dynamodbgeo.PutPointInput(
            dynamodbgeo.GeoPoint(float(data['latitude']),float(data['longitude'])),  # latitude then latitude longitude
            str(uuid.uuid4()),  # Use this to ensure uniqueness of the hash/range pairs.
            PutItemInput  # pass the dict here
        ))

print('debug')
QueryRadiusInput={    }

query_reduis_result=geoDataManager.queryRadius(
    dynamodbgeo.QueryRadiusRequest(
        dynamodbgeo.GeoPoint(53.339428, -6.257664), # center point and radius is in meters
        100000, QueryRadiusInput, sort = True)) # diameter
print(query_reduis_result)

for customer in query_reduis_result:
  print(customer['user_id'],',',customer['name'])

