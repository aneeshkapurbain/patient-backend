import boto3
import base64
from botocore.exceptions import ClientError


class SecretManager:
    """ class to retrieve secret key using secretmanager from AWS """
    def __init__(self):
        """ Initialize SecretManager """
        # region name
        region_name = "eu-central-1"

        # Create a Secrets Manager client
        session = boto3.session.Session()
        self.client = session.client(
            service_name='secretsmanager',
            region_name=region_name
        )

    def get_secret(self, secret_name):
        """ get secret key value
            :input:
                secret_name: str
            :outut:
                decoded str
        """
        secret = None
        try:
            get_secret_value_response = self.client.get_secret_value(
                SecretId=secret_name
            )
        except ClientError as err:
            print(f'Cannot fetch DB password from secret manager: {err}')
        else:
            if 'SecretString' in get_secret_value_response:
                secret = get_secret_value_response['SecretString']
            else:
                secret = base64.b64decode(get_secret_value_response['SecretBinary'])
        return secret
