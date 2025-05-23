# testplant.py
# this is a test file to check the plantservice.py functionality
# the plants are based off the plantservice data
# disclaimer, the plant data is only for testing
import time

def get_plant_image(plant_name):
    """Get a plant image by name"""
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
# these are just sample plants for testing, more options for the microservice will be implemented
def print_available_plants():
    """Print the list of available plants"""
    print("\nAvailable plants:")
    print("- bamboo")
    print("- cactus")
    print("- pine")
    print("- orchids")


def main():
    """Main test function"""
    print("Plant Image Service")
    print("=====================================")
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
            plant_name = input("Enter plant name: ").strip().lower()
            get_plant_image(plant_name)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Enter 1, 2, or 3.")

if __name__ == "__main__":
    main()