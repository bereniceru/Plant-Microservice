# plantservice.py
# plant image service
# Just provide a plant name, get an image path
# still working on the rest of the implementation, it will have species, genus, and more relevant functionality

import time
import os

# Sample plant database, will link images to the plants
# more details and functions will be added like genus, etc
PLANTS = {
    "bamboo": "images/bamboo.jpg",
    "cactus": "images/cactus.jpg",
    "pine": "images/pine.jpg",
    "orchids": "images/orchids.jpg"
}

print("Plant Image Service is running...")

# create images folder if it doesn't exist
IMAGES_FOLDER = "images"
if not os.path.exists(IMAGES_FOLDER):
    os.makedirs(IMAGES_FOLDER)
    print(f"Created {IMAGES_FOLDER} directory")
    
    # this is a placeholder, if the plan name is relevant to the DATA it should generate a path
    for plant_name, path in PLANTS.items():
        with open(path, "w") as f:
            f.write(f"Placeholder for {plant_name} image\n")
            f.write("Replace with actual .jpg image file\n")
    
    print("Created sample placeholder images")

print("Waiting for plant-service.txt")
    
# main loop
while True:
    time.sleep(1)  # check every second (i might change the seconds)
    
    try:
        # read data from the service file
        with open("plant-service.txt", "r") as file:
            content = file.read().strip().lower()
        
        # If file is empty or already contains an image path, skip
        if not content or content.startswith("images/") or content.startswith("error:"):
            continue
        
        print(f"Processing request: '{content}'")
        
        # look up the plant name
        if content in PLANTS:
            # plant found, return image path
            image_path = PLANTS[content]
            print(f"Found image: {image_path}")
            with open("plant-service.txt", "w") as file:
                file.write(image_path)
        else:
            # plant not found, error
            print(f"Plant not found: '{content}'")
            with open("plant-service.txt", "w") as file:
                file.write(f"error:Plant not found: {content}")
            
    except FileNotFoundError:
        # create file if not found
        with open("plant-service.txt", "w") as file:
            file.write("")
        print("Created plant-service.txt file")
    except Exception as e:
        print(f"Error: {e}")
        try:
            with open("plant-service.txt", "w") as file:
                file.write(f"error:{str(e)}")
        except:
            pass