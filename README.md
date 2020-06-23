# besu-image-service
## Description
This repository contains the code for a simple web service to manipulate images. It's made to be easily deployed to Google Cloud Run.

## Functionality
* Add text to an image supplied by URL parameters
  * Position, color and parameter name are configurable via json files
  * Fonts will be changeable in the future
* Add multiple other extras:
  * Images
  * Progressbars

## How To
* Place the base images in the /static/images directory
* [Set the environment variables](https://cloud.google.com/run/docs/configuring/environment-variables) for extra configurations
* Create a configuration file for each image with the same name (just ending in json) in the /static/layouts directory
* Run the service and access the image via its name, combined with the defined parameters
