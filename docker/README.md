# README
## SOPGUI
SOPGUI ist ein Programm zur Erstellung und Bearbeitung von Standard Operating Procedures (SOPs).

## Container starten

### Programm-Container
+ Verzeichnisordner: docker/DockerSOPGUI
+ Imagegröße: 1.03 GB


| Anweisung               | Dockerbefehl                                                                                                                                                                                                                                                        | script                |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| Aufbau des Image       | docker build -t sopgui .                                                                                                                                                                                                                                            | build_docker_image.sh |
| Starten des Containers | docker run --rm -it -v "$(pwd)/output":/home/sopautor/output -v "$(pwd)/database":/home/sopautor/database -v"/etc/timezone":"/etc/timezone":ro -v"/etc/localtime":"/etc/localtime":ro --net=host --env="DISPLAY" -v "$HOME/.Xauthority:/root/.Xauthority:ro" sopgui | run_container.sh      |



### Datenbank-Container
+ Verzeichnisordner: docker/DockerMongo
+ Imagegröße: 98.0 MB
+ Shell öffnet sich in neuem Fenster mit Aufforderung zur Passworteingabe.


| Anweisung                        | Dockerbefehl                                                                                                         | script |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------|------|
| **Aufbau des Image**             | docker pull mongo:4.2                                                                                                | N/A    |
| **Starten des Containers**       | docker run -p 27017:27017 -d -v "$(pwd)/datadb":/data/db --name sop-mongo                                            | N/A    |
| **Start nach Authentifikation** | docker run -p 27017:27017 -d -v "$(pwd)/datadb":/data/db --name sop-mongo --restart=unless-stopped mongo:4.2  --auth | run_mongo_server.sh    |
| **Start der Mongo Shell**       | konsole -e docker exec -it sop-mongo bash -c "mongo -u [Benutzername] -p"                                            | connect.sh    |                                                                                          
