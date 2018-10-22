
import boto3

class RekognitionAWSClient(object):
    def __init__(self,aws_access_key_id,aws_secret_access_key,region_name, *args, **kwargs):
        self.aws_access_key_id=aws_access_key_id
        self.aws_secret_access_key=aws_secret_access_key
        self.region_name=region_name

    def getRekognitionClient(self):

        rekognition = boto3.client('rekognition',
        aws_access_key_id=self.aws_access_key_id,
        aws_secret_access_key=self.aws_secret_access_key,
        region_name=self.region_name)

        return rekognition

    def detect_text(self,image):
        return self.getRekognitionClient().detect_text(Image={'Bytes': image})

