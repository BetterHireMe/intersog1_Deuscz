# Intersog: Junior Python Developer task
With this application you can check events that occures in your filesystem.

## Getting Started
You can use this application using pure Python 3 or using Docker.

## An example of using an application
Firstly you need to install some dependencies:

```
$ pip install watchdog
```
1. Clone this repository.

2. Change settings in 'settings.py' :

```
# Enter your path here
PATH = "."  # Example "C:\\your_path\\"

# Enter time format you want to display

TIMEFORMAT = '%Y-%m-%d %H:%M:%S' #Default '%Y-%m-%d %H:%M:%S'

# Select the type of events you want to display
MOVED_FILES_OR_FOLDERS = True
MODIFIED_FILES_OR_FOLDERS = True
CREATED_FILES_OR_FOLDERS = True
DELETED_FILES_OR_FOLDERS = True

```

3. Then just start app:
```
$ python eventobserver.py
```

## You can also use this application with docker

1. Clone this repository.
2. Change folders that you will be use in Dockerfile and settings.py.
Dockerfile:
```
COPY . /app/
WORKDIR /app/
```
settings.py:
```
PATH = "your_path"
```
3. Build the image:
```
$ docker build -t yourappname .
```
4. Run image:
$ docker run yourappname
5. To do some changes and to see how this application works, we need to connect to this docker session.
For this open new terminal and type:
```
$ docker exec -i -t your_image_id /bin/bash
```
Where 'your_image_id' is an id of the image. You can find out it by typing:
```
$ docker ps
```

## Status
Project is: _in progress_
## Contact
Email: Robert355335@gmail.com