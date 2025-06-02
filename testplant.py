# testplant.py
# this is a test file to check the plantservice.py functionality
# now supports both common names and genus:species format
# disclaimer, the plant data is only for testing
import time

def get_plant_image(plant_name):
    ## get a plant image by name or genus:species
    print(f"\nLooking up image for plant: '{plant_name}'")
    
    # write plant name to communication file
    with open("plant-service.txt", "w") as file:
        file.write(plant_name)
    
    # wait 2 seconds.. service in process
    print("Waiting for service to respond...")
    time.sleep(2)
    
    # Read the response
    with open("plant-service.txt", "r") as file:
        response = file.read().strip()
    
    # Process the response
    if response.startswith("error:"):
        error_message = response[6:]  
        print(f"Error: {error_message}")
        return None
    else:
        print(f"Found image: {response}")
        
        try:
            # open or read images 
            with open(response, "r") as f:
                content = f.read()
            print(f"\nImage placeholder content:\n{content}")
        except FileNotFoundError:
            print("Image file not found..")
        except Exception as e:
            print(f"Error reading image: {e}")
        
        return response


## hardcoded lines were removed
## the available plant function should only show things in the images folder


def print_available_plants():
    """Print the list of available plants"""
    import os
    print("\nAvailable plants:")
    
    if os.path.exists("images"):
        plants = []
        for filename in os.listdir("images"):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                name = os.path.splitext(filename)[0]
                plants.append(f"- {name}")
        
        if plants:
            for plant in sorted(plants):
                print(plant)
        else:
            print("No plant images found in images folder")
    else:
        print("Images folder not found")

    # when clicking option 2 you can also search with a genus:species format
    # theres are examples of what can be inputted
    # bambusa:vulgaris
    # cactaceae:varied

def main():
    """Main test function"""
    print("Plant Image Service")
    print("☆  ☆  ☆  ☆  ☆  ☆  ☆")
    print("This test will demonstrate a plant image retrieval service")
   
    
    # this will double check that there is a plant-service.txt available
    try:
        open("plant-service.txt", "r").close()
    except FileNotFoundError:
        try:
            open("plant-service.txt", "w").close()
            print("Created plant-service.txt.")
        except Exception as e:
            print(f"Error creating plant-service.txt!: {e}")
            return
    
    while True:
        print("\nCommands:")
        print("1. Display All Plants")
        print("2. Search Plant Up")
        print("3. Exit Plant Image Service")
        
        choice = input("\nEnter one of the following choices (1-3): ")
        
        if choice == "1":
            print_available_plants()
        elif choice == "2":
            plant_name = input("Enter plant name or genus:species: ").strip().lower()
            get_plant_image(plant_name)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
