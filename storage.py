import io
import json
import os

from PIL import Image
from google.cloud import storage


def get_config(config_name):
    stage = os.getenv('STAGE', 'dev')
    if stage == 'prod':
        bucket_name = os.getenv('BUCKET_NAME')
        client = storage.Client()
        bucket = client.get_bucket(bucket_name)
        blob = bucket.get_blob('static/layouts/' + config_name + '.json')
        json_file = blob.download_as_string()
        json_file = json_file.decode("utf-8")
        data = json.loads(json_file)
        return data
    elif stage == 'dev':
        print("Running in dev environment, loading config from local file system")
        with open('static/layouts/' + config_name + '.json') as json_file:
            data = json.load(json_file)
            return data


def get_image(image_name):
    stage = os.getenv('STAGE', 'dev')
    if stage == 'prod':
        bucket_name = os.getenv('BUCKET_NAME')
        client = storage.Client()
        bucket = client.get_bucket(bucket_name)
        image_blob = bucket.get_blob('static/images/' + image_name).download_as_string()
        img_bytes = io.BytesIO(image_blob)
        return Image.open(img_bytes)
    elif stage == 'dev':
        print("Running in dev environment, loading image from local file system")
        return Image.open('static/images/' + image_name)
