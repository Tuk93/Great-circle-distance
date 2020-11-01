from math import radians, degrees, sin, cos, asin, acos, sqrt
import json
import boto3
import dynamodbgeo
import uuid

dynamodb = boto3.client('dynamodb', region_name='us-east-1')

config = dynamodbgeo.GeoDataManagerConfiguration(dynamodb, 'geo_test')

geoDataManager = dynamodbgeo.GeoDataManager(config)

config.hashKeyLength = 7

# Use GeoTableUtil to help construct a CreateTableInput.

table_util = dynamodbgeo.GeoTableUtil(config)
create_table_input=table_util.getCreateTableRequest()

#tweaking the base table parameters as a dict

create_table_input["ProvisionedThroughput"]['ReadCapacityUnits']=5

# Use GeoTableUtil to create the table

table_util.create_table(create_table_input)

dub_lat2 = 53.339428
dub_lon2 = -6.257664

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

