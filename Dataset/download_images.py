"""
Images can be found using their fileId (located under the attribute 'media') in: 
https://bucket-image-easy-experience-cover-resized.s3.eu-west-1.amazonaws.com/resized-cover-{{photo}}.200.jpeg
"""

import json
import boto3  # pip install boto3

schede_path = "/home/gianfree/Desktop/Thesis/Notes and code/Dataset/kuriu-schede-2022-06JUN-18.json"
url = "https://bucket-image-easy-experience-cover-resized.s3.eu-west-1.amazonaws.com/resized-cover-"
download_path = "/home/gianfree/Desktop/Thesis/Notes and code/Dataset/images/"

f = open(schede_path)
json_file = json.load(f)

#get and print list of buckets
s3 = boto3.client("s3")
response = s3.list_buckets()
buckets = [bucket["Name"] for bucket in response["Buckets"]]
print("Bucket list: {}".format(buckets))

#Download Images
s3 = boto3.resource("s3")
my_bucket = s3.Bucket("bucket-image-easy-experience-cover")

count = 0
for s3_obj in my_bucket.objects.all():
    #print(s3_obj)
    if "/" in s3_obj.key:
        print(s3_obj.key + " is a directry")
        continue
    else:
        my_bucket.download_file(s3_obj.key, download_path + s3_obj.key)
        #print("Image: {}".format(s3_obj.key))
        count += 1

print("Number of downloaded images: {}".format(count))
