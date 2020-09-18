import io
import json
import os

from PIL import Image, ImageFont
from google.cloud import storage

stage = os.getenv('STAGE', 'dev')
if stage == 'prod':
    bucket_name = os.getenv('BUCKET_NAME', "serpent-bucket")
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)


def get_file_from_bucket(path):
    blob = bucket.get_blob(path)
    blob_string = blob.download_as_string()
    return blob_string


def get_config(config_name):
    if stage == 'prod':
        json_file = get_file_from_bucket('static/layouts/' + config_name + '.json')
        data = json.loads(json_file)
        return data
    elif stage == 'dev':
        print("Running in dev environment, loading config from local file system")
        with open('static/layouts/' + str(config_name) + '.json') as json_file:
            data = json.load(json_file)
            return data


def get_image(image_name):
    if stage == 'prod':
        image_blob = bucket.get_blob('static/images/' + image_name).download_as_string()
        # blob_string = blob
        # image_blob = get_file_from_bucket('static/images/' + image_name)
        img_bytes = io.BytesIO(image_blob)
        img = Image.open(img_bytes)
    elif stage == 'dev':
        print("Running in dev environment, loading image from local file system")
        img = Image.open('static/images/' + image_name)

    # Fix image encoding
    background = Image.new("RGBA", img.size, (255, 255, 255))
    background.paste(img)
    img = background

    return img


def get_font(font_name, font_size):
    if stage == 'prod':
        font_blob = get_file_from_bucket('static/fonts/' + font_name + '.ttf')
        font_bytes = io.BytesIO(font_blob)
        return ImageFont.truetype(font_bytes, font_size)
    elif stage == 'dev':
        print("Running in dev environment, loading font from local file system")
        try:
            return ImageFont.truetype('static/fonts/' + font_name + '.ttf', font_size)
        except OSError:
            print("Can't find font! Loading default font")
            return ImageFont.load_default()