import json
import boto3
import string
from secrets import token_urlsafe

def lambda_handler(event, context):

    # Define a new secret
    pass_length = 24
    newPassword = token_urlsafe(pass_length)
    
    client = boto3.client('secretsmanager')

    # Get the secret
    getRes = client.get_secret_value(
        SecretId = 'SecretName' 
    )
    current_secrets = json.loads(getRes['SecretString'])
 
    # Update the password with the new one
    # "password" is the value name of the pass in the secret
    current_secrets.update({
        "password" : newPassword
    })
    
    # Store the new password in the secret
    response = client.put_secret_value(
        SecretId = 'SecretName',
        SecretString=str(json.dumps(current_secrets))
    )

