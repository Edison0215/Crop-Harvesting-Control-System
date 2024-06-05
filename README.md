# Crop Harvesting Control System
This repository consists of python codes for the prototype development of an automated crop harvesting system using Raspberry Pi. 
The python codes are only act as a website protoype of devleoping a website in controlling a 3 DOF stepper motor collect readily harvested crops via a clamp.

## Declaration 
This code is modifed by taking source codes from https://github.com/techwithtim/Flask-Web-App-Tutorial as reference.

## To Run The Website
- Download this folder
- Open cmd in the folder's directory
- ```pip install flask```
- ```pip install flask_login```
- execute the python code: ```python main.py```
- The website link will be shown in the cmd terminal
- Direct to the website link via web browser
- Access the website using username: ```admin``` and password: ```1234```

## man2.0.py
- Current python code ```main.py ``` is taking ```man.py``` library as default.
- ```man2.0.py``` is utlized to display livestream video of the crops via Rasberry Pi camera in the website.
-  ```xaxis.py``` (used in man2.0.py) is not available in this repository. (It is used to change the clockwise, anticlockwise and stopping motion of the stepper motor in each x, y, z direction, opening and closing the clamp.)
