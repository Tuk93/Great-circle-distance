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

