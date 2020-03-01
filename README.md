# dockerproj
This is my Docker Container Project for the Cloud Computing Spring 2020 class.
I have created a docker container that deploys a simple Hello function: it take two arguments - user's name and location, and greets them accordingly.

In this video I show how to pull the image down and run it on AWS Cloud9.
To pull and run the image on Cloud9, use

docker pull juliaoblasova/app:hello
docker run -it juliaoblasova/app:hello bash
python app.py



