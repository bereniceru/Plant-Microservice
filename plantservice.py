# plantservice.py
# plant image service
# Just provide a plant name, get an image path
# also takes "genus:species" format

import time
import os

# sample plant function 
# added Genus:species 
def get_plants():
    plants = {}
    
    # add any files found in images folder
    if os.path.exists("images"):
        for filename in os.listdir("images"):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):

                # Use filename without extension 
                name = os.path.splitext(filename)[0].lower()
                plants[name] = f"images/{filename}"
    
    return plants

print("Plant Image Service is running...")

# create images folder if it doesn't exist
IMAGES_FOLDER = "images"
if not os.path.exists(IMAGES_FOLDER):
    os.makedirs(IMAGES_FOLDER)
    print(f"Created {IMAGES_FOLDER} directory")

print("Waiting for plant-service.txt")
    
# main loop
while True:
    time.sleep(5)  # check every second (i might change the seconds)
    
    try:
        # read data from the service file
        with open("plant-service.txt", "r") as file:
            content = file.read().strip().lower()
        
        # If file is empty or already contains an image path, skip
        if not content or content.startswith("images/") or content.startswith("error:"):
            continue
        
        print(f"Processing request: '{content}'")
        
        # Get current plants from folder
        PLANTS = get_plants()
        
        # look up the plant name (now works with genus:species too)
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
