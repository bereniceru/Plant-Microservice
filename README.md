# Plant-Microservice
microservice implementation for a plant image service

# Request plant (genus, species) information
To request an image by name write the name to the plant-service.txt file by running the plantservice program in a terminal first

example code with "bamboo" as the example name
with open("plant-service.txt", "w") as file:
    file.write("bamboo")

# Receive plant information
To receive genus or species information wait a few seconds after the request, if there is a plant on the database the response will be a path to the desired image. "Error" will be displayed if nothing was found. The name will also be displayed in the plant-service.txt file for reference

![UML Sequence Diagram](UML%20Plant%20Microservice.png) 

