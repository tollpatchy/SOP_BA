#!/bin/bash
## grants access access for xserver to docker temporarily 
xhost +local:docker
docker run --rm -it -v "$(pwd)/output":/home/sopautor/output:rw -v "$(pwd)/data":/home/sopautor/data:rw -v"/etc/timezone":"/etc/timezone":ro -v"/etc/localtime":"/etc/localtime":ro -v /tmp/.X11-unix:/tmp/.X11-unix --env="DISPLAY" sopgui
xhost -local:docker
