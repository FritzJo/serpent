# 🐍 Serpent (Serverless Picture Enrichment Toolkit)
![serpent overview](doc/images/serpent_overview.png "Basic Structure of Serpent")
## Description
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/661e7a4b392d4bc78d1959779a4bfb15)](https://www.codacy.com/manual/fritzjo-git/serpent?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=FritzJo/serpent&amp;utm_campaign=Badge_Grade)

This repository contains the code for a simple web service to create dynamically customized images. Textfields and other extras are defined in configuration files and their content can be assigned for each request by using URL parameters!
It's made to be easily deployed to Google Cloud Run to provide custom embeddable images at minimal cost.

## Functionality
* Add text to an image
  * Flexible content of each textfield, defined by URL parameters
  * Position, font, color and parameter name are configurable via json files
* Add overlay-images
* Add simple progress bars

## Configuration
Serpent uses a json file to describe all changes that will be made to a given image. These files are called *layouts*. An example can be found in [```static/layouts/example.json```](static/layouts/example.json).

To get further information about all options and the structure of layouts: Check out the [documentation](doc/Configuration.md)

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
Its generally recommended to use a virtual environment, instead of installing all packages globally. You can find more information on how to do that [here](https://docs.python.org/3/tutorial/venv.html)
#### Docker
``` bash
git clone https://github.com/FritzJo/serpent.git
cd serpent
docker build -t serpent .
docker run  -p 5000:5000 serpent
```

After successfully deploying the application you can test if everything is working by opening the following link in your browser:
[```http://localhost:5000/example.png?text=HelloWorld```](http://localhost:5000/example.png?text=HelloWorld)

You should see [this image](doc/result.png)

### Google Cloud Plattform
* Create Google Cloud Account
* Create a Project
* Open [Cloud Source Repositories](https://source.cloud.google.com/) and add a new Repository
    * Add a repository
    * Connect external repository
    * Select your project and GitHub as a Git provider
    * Connect to GitHub
* Configure the automatic build pipeline
    * Open [Cloud Build](https://console.cloud.google.com/cloud-build/dashboard)
    * Select "Triggers" and create a new trigger
    * Choose the repository from the last step and set the branch to master
    * Use "Cloud Build configuration file" as configuration (it's located in the root directory [```/cloudbuild.yaml```](/cloudbuild.yaml))
    * Run the trigger once manually
    * It's totally normal for the service to fail to start (because its still missing environment variables, we will fix that in a later step)
* Storage setup
    * Images and layouts will be located in [Google Cloud Storage](https://console.cloud.google.com/storage/browser)
    * Create a new bucket
    * Create the following folder structure
    
    ```
    static/
        fonts/
        images/
        layouts/
    ```
* Go to [Google Cloud Run](https://console.cloud.google.com/run)
    * The pipeline should have created the service
        * If not, create a new service
        * Select a region and service name
        * Select the serpent image 
    * Edit the service
        * Check if the container port is 5000
        * Select "Variables" and create the following
    ```
    STAGE=prod
    BUCKET_NAME=<your-bucket-name>
    ```
    * Click "Deploy"!
## FAQ
### 1. What are the restrictions in a local deployment
* Images can't be loaded from remote locations and have to be placed in the [```static/images```](static/images) folder.
* Same goes for layouts ( [```static/layouts```](static/images))
* If you use Docker, you have to build a new docker image for every change in configuration (and for each added image)
* The flask backend runs in development mode and therefor only supports very few simultaneous connections.
* This tool is developed with GCP in mind and only tested for that environment.
