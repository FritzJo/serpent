# 🐍 Serpent (Serverless Picture Enrichment Toolkit)
## Description
This repository contains the code for a simple web service to manipulate images. It's made to be easily deployed to Google Cloud Run to provide custom embeddable images with minimal cost.

## Functionality
* Add text to an image
  * Flexible content of each textfield, defined by URL parameters
  * Position, font, color and parameter name are configurable via json files
* Add overlay-images
* Add simple progress bars

## Deployment
Serpent supports two major options for deployment: local and on [GCP](https://cloud.google.com). The local deployment should only be used for development and testing purposes. You could still run it in production with limitations regarding flexibility and performance.
### Local
#### Python
``` bash
git clone https://github.com/FritzJo/serpent.git
cd serpent
pip install -r requirements.txt
python app.py
```
Its generally recommended to use a virtual environment, instead of installing all packages globally. You can find more information on how to do thate [here](https://docs.python.org/3/tutorial/venv.html)
#### Docker
``` bash
git clone https://github.com/FritzJo/serpent.git
cd serpent
docker build -t serpent .
docker run  -p 5000:5000 serpent
```

### Google Cloud Plattform
TODO

## FAQ
### 1. What are the restrictions in a local deployment
* Images can't be loaded from remote locations and have to be placed in the [```static/images```](static/images) folder.
* Same goes for layouts ( [```static/layouts```](static/images))
* If you use Docker, you have to build a new docker image for every change in configuration (and for each added image)
* The flask backend runs in development mode and therefor only supports very few simultaneous connections.
* This tool is developed with GCP in mind and only tested for that environment.