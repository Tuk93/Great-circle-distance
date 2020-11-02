#  Great-circle-distance and DynamoDB Geo to calculate to calculate distance of two locations on Earth.

This repository contains one of the ways of geographic calculation and we can calculate distance of two locations on Earth using Python.We have several mathematical formulaes to calculate the distance, in this repository we will be covering Great-circle-distance method.

Our formula will take inputs as GPS coordinates (latitude, longitude), and return the approximately distance and based on that distance we can take our future business decisions.

### First method:

#### The Great-Circle Distance :

The Great Circle distance formula computes the shortest distance path of two points on the surface of the sphere. That means, when applies this to calculate distance of two locations on Earth, the formula assumes that the Earth is spherical.

https://en.wikipedia.org/wiki/Great-circle_distance

The radius r value for this spherical Earth formula is approximately ~6371 km(If you want to use miles, replace 6371 with 3958.756).

### Installation and How to run this demo locally before deploying it into production :

1.Clone the repo :

   ##### git clone https://github.com/Tuk93/Great-circle-distance.git

2.Change your directory to the cloned repo.

3.First you can run the python file reader.py which reads the customer.json file and reads each customer entry (one per line) to calculate the distance of customer from our dublin office and returns the list of customer id and names who are within 100km range from our dublin office.

### python reader.py

4.Our distance.py file contains the programme to calculate distance of two locations based on GPS coordinates.


### Second method:

Using Geo Library for Amazon DynamoDB to query geospatial data using Amazon DynamoDB.(unofficial port of https://github.com/awslabs/dynamodb-geo), we will be using feature Radius Queries which Returns all of the items that are within a given radius of a geo point.

##Installation :

#### pip install s2sphere
#### pip install boto3
#### pip install dynamodbgeo

Go to the dynamodbgeo folder, Once you installed the above packages please run :

### python querytable.py

This file will import the AWS sdk and set up your DynamoDB connection, create a table in your AWS account in us-east-1 region with name geo-test.Once the table is created it will assign 5WCU/RCU cost efficient throughput (we can decrease it further once we are done with our testing).

Additionally we can test the same by Setting Up DynamoDB Local (Downloadable Version) Having this local version helps you save on throughput, data storage, and data transfer fees. In addition, you don't need an internet connection while you develop your application. 

For more information on setting it up locally, please follow official AWS dynamodb guidelines and steps :[dynamodb docs] (https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html)

Once you setup a table it will read customer.json file and add items in your Dynamodb table(geo-test) including primary key which it will create dynamically, as we want to return user_id and customer name in our final result so i have inserted corresponding fields with GPS coordinates (geoJson) in our table.


 ```python
#preparing non key attributes for the item to add

 PutItemInput = {
            'Item': {
                'user_id': {'S': data['user_id']},
                'name': {'S': data['name']}
            }
        }
        
        geoDataManager.put_Point(dynamodbgeo.PutPointInput(
            dynamodbgeo.GeoPoint(data['latitude'],data['longitude']),  # latitude then  longitude
            str(uuid.uuid4()),  # Use this to ensure uniqueness of the hash/range pairs.
            PutItemInput  # pass the dict here
        ))

```

please find sample entry from our geo-test Dynamodb table:

{
  "geohash": 5206934354372931255,
  "geoJson": "52.240382,-6.972413",
  "hashKey": 5206934,
  "name": "Customer-name",
  "rangeKey": "a7121176-a419-4f54-9a99-712460d5266b",
  "user_id": 10
}

Sample query from geo library:

query_reduis_result=geoDataManager.queryRadius(
    dynamodbgeo.QueryRadiusRequest(
        dynamodbgeo.GeoPoint(dub_lat2, dub_lon2), # dub office point
        100000, QueryRadiusInput, sort = True)) # radius in meters


