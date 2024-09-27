class ParkingSystem:
    def __init__(self, total_spots):
        self.total_spots = total_spots
        self.available_spots = total_spots
        self.parking_lot = {}
        
    def register_user(self, user_id, vehicle_number):
        if user_id not in self.parking_lot:
            self.parking_lot[user_id]=vehicle_number
            print(f"User{user_id} registered with number{vehicle_number}")
        else:
            print("user already registered")
            
    def park_vehicle(self, user_id):
        if user_id in self.parking_lot:
            if self.available_spots > 0:
                self.available_spots -=1
                print(f"vehicle parked for user {user_id}. {self.available_spots} spots left.")
            else:
                print("no available spots")
        else:
            print("user not registered")
            
    def remove_vehicle(self, user_id):
        if user_id in self.parking_lot:
            self.available_spots +=1
            print(f"vehicle removed for user {user_id}.{self.available_spots} spots available")
        else:
            print("user not registered")

    def is_valid_user_id(self, user_id):
        return user_id in self.parking_lot

    def is_valid_vehicle_number(self, vehicle_number):
        #add validation logic here
        return len(vehicle_number)
#example usage:
total_spots = int(input("Enter total parking slots:"))
parking = ParkingSystem(total_spots)

while True:
    print("\n1. Register User")
    print("2. Park Vehicle")
    print("3. Remove Vehicle")
    print("4. Exit")
    print("5. Check User ID Validity")
    print("6. Check Vehicle number Validity")
    choice = input("Enter your choice: ")

    if choice == "1":
        user_id = input("Enter User ID: ")
        vehicle_number = input("Enter Vehicle Number: ")
        parking.register_user(user_id, vehicle_number)
    elif choice == "2":
        user_id = input("Enter user ID: ")
        if parking.is_valid_user_id(user_id):
            parking.park_vehicle(user_id)
        else:
            print("Invalid User ID")
    elif choice == "3":
        user_id = input("Enter User ID: ")
        if parking.is_valid_user_id(user_id):
            parking.remove_vehicle(user_id)
        else:
            print("Invalid user ID")
    elif choice == "4":
        print("Existing...")
        break
    elif choice == "5":
        user_id = input("Enter User ID: ")
        if parking.is_valid_user_id(user_id):
            print("Valid User ID")
        else:
            print("Invalid user ID")
    elif choice == "6":
        vehicle_number = input("Enter vehicle number: ")
        if parking.is_valid_vehicle_number(vehicle_number):
            print("valid vehicle number")
        else:
            print("Invalid vehicle number")
    else:
        print("Invalid choice. Please try again.")
            
    
            
        
    
                
                
