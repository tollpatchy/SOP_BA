#!/bin/bash
#set -eEuo pipefail
#umask 022
docker build --build-arg USER_ID=$(id -u ${USER}) -t sopgui .
