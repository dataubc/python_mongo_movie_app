# How to run the program:
 ## Using command line
- pip install -r requirements.txt
- python mongo.py

## Using docker
- Clone the repo localy
- Go to the root of the repo folder
- To build the image run the following command:
`docker build -t mongo .`
- Run the following commans to creat the container
`docker run -p 8899:8899 mongo`
- To access the mongo notebook, open this file in a browser with the given link in the broswer,it will be something like this
`http://127.0.0.1:8899/?token=xxxxx`