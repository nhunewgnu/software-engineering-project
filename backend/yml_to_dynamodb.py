import boto3
import yaml

# Load the YAML data
with open('unibot.yml', 'r') as file:
    yml_data = yaml.safe_load(file)

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name ='us-east-1')

# Create the Intents table
intents_table = dynamodb.create_table(
    TableName='Intents',
    KeySchema=[
        {'AttributeName': 'id', 'KeyType': 'HASH'}
    ],
    AttributeDefinitions=[
        {'AttributeName': 'id', 'AttributeType': 'S'}
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
)

# Wait for the table to be created
intents_table.meta.client.get_waiter('table_exists').wait(TableName='Intents')

# Create the Responses table
responses_table = dynamodb.create_table(
    TableName='Responses',
    KeySchema=[
        {'AttributeName': 'id', 'KeyType': 'HASH'}
    ],
    AttributeDefinitions=[
        {'AttributeName': 'id', 'AttributeType': 'S'}
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
)

# Wait for the table to be created
responses_table.meta.client.get_waiter('table_exists').wait(TableName='Responses')

# Insert intents and responses data into the tables
for intent, examples in yml_data['intents'].items():
    # Add intent to the Intents table
    intents_table.put_item(
        Item={
            'id': intent,
            'examples': examples['examples']
        }
    )

    # Add the corresponding response to the Responses table
    response_key = f"utter_{intent}"
    if response_key in yml_data['responses']:
        responses_table.put_item(
            Item={
                'id': response_key,
                'text': yml_data['responses'][response_key][0]['text']
            }
        )
