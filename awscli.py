import boto3
from botocore.exceptions import ClientError
import logging

class AWSPY(object):
    def __init__(self , aws_key,aws_secret , aws_bucket):
        ''' Configure for aws creadentials '''
        self.aws_session = boto3.Session(
                aws_access_key_id="AKIA44LLCFCGJ6HUCRGX",
                aws_secret_access_key="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")
        self.aws_bucket = aws_bucket
    
    def is_aws_conf(self):
        if(self.aws_session):
            # self.downLoad_Files()
            return True
        else:
            print("Permission Denied")
            return False

    def upload_file(self, file_name, bucket, object_name=None):
        """Upload a file to an S3 bucket
        @param: file_name: File to upload
        @param: bucket: Bucket to upload to
        @param: object_name: S3 object name. If not specified then file_name is used
        @return: True if file was uploaded, else False
        """
        # If S3 object_name was not specified, use file_name
        if object_name is None:
            object_name = file_name

        # Upload the file
        s3_client = self.aws_session.client('s3')
        try:
            response = s3_client.upload_file(file_name, bucket, object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True
        
    ''' Get the List of S3 Bucket Details'''
    def get_S3_Details(self):
        # Let's use Amazon S3
        s3 = self.aws_session.resource('s3')
        # Print out bucket names
        for bucket in s3.buckets.all():
            if bucket.name=='aimdev-tool':
                data = open('/home/trinath/Downloads/face.jpg', 'rb')
                is_uploaded = self.upload_file('/home/trinath/Downloads/face.jpg',bucket.name,'face.jpg')
                if(is_uploaded):
                    print("File {} uploaded to {} bucket".format('filenamee',bucket.name))
                else:
                    print("Unable to upload file to {} bucket".format(bucket.name))

    def check_Permissions(self):
        # Retrieve a bucket's ACL
        s3 = self.aws_session.client('s3')
        result = s3.get_bucket_acl(Bucket=self.aws_bucket)
        print(result)

    def donwload_Permissions(self,file_name):
        s3 = self.aws_session.client('s3')
        with open(file_name, 'wb') as f:
            s3.download_fileobj(self.aws_bucket, file_name, f)
# if __name__ == "__main__":
#     is_aws_conf = set_aws_credentials("aws_key","aws_secret")
#     if(is_aws_conf):
#         # get_S3_Details() 
#         downLoad_Files()
#     else:
#         print("Permission Denied")


