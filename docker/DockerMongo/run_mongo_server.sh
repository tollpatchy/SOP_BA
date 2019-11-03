#!/bin/bash
#set -eEuo pipefail
#umask 022

docker run -p 27017:27017 -d -v "$(pwd)/datadb":/data/db --name sop-mongo --restart=unless-stopped mongo:4.2  --auth

# https://docs.docker.com/config/containers/start-containers-automatically
#--restart=unless-stopped 
#--hostname mongo 
