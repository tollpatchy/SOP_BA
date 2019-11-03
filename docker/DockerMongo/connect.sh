#!/bin/bash
#set -eEuo pipefail
#umask 022
#konsole -e docker exec -it sop-mongo mongo
konsole -e docker exec -it sop-mongo bash -c "mongo -u myUserAdmin -p"
