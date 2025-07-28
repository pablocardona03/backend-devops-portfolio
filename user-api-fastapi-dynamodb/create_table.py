import boto3
from botocore.exceptions import ClientError

# !!!! AWS CONFIGURE NECESARY !!!!
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')



def create_users_table():
    try:
        table = dynamodb.create_table(
            TableName='users',
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'  
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S' 
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        print("Creating table...")
        table.meta.client.get_waiter('table_exists').wait(TableName='users')
        print("Table created successfully ✅")
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceInUseException':
            print("⚠️ Table already exists.")
        else:
            print(f"❌ Error: {e}")

if __name__ == '__main__':
    create_users_table()
