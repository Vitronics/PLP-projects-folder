def get_person_info(): 
    person = {}
    person ["name:"]  = input("Enter your name: ")
    person ["age:"] = int(input ("Enter age :"))
    person ["Favourite_color:"] = input("Enter Favourite color: ")
    return person

def display_person_info(person_dict):
    print("\nPersonal Information")
    for key, value in person_dict.items():
        print(f"{key.capitalize()} {value}")

def main():
    # Get the person's information
    person_info = get_person_info()
    
    # Display the person's information
    display_person_info(person_info)

# Run the main function
if __name__ == "__main__":
    main()