class ParkingSystem:
    def __init__(self,total_spots):
        self.total_spots = total_spots
        self.available_spots = total_spots
        self.parking_lot = {}
    def user_student(self, user_id, vehicle_number,valid_date):
        if user_id not in self.parking_lot:
            self.parking_lot[user_id]=vehicle_number
            print(f"User {user_id} registered with number {vehicle_number}")
            print("Registered as student")
        else:
            print("user already registered")
    def user_faculty(self, user_id, vehicle_number,valid_date):
        if user_id not in self.parking_lot:
            self.parking_lot[user_id]=vehicle_number
            print(f"User {user_id} registered with number {vehicle_number}")
            print("Registered as faculty")
        else:
            print("user already registered")
    def user_guest(self, user_id, vehicle_number,valid_date):
        if user_id not in self.parking_lot:
            self.parking_lot[user_id]=vehicle_number
            print(f"User {user_id} registered with number {vehicle_number}")
            print("Registered as guest")
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
        return len(vehicle_number)
total_spots = int(input("Enter total parking slots:"))
parking = ParkingSystem(total_spots)
while True:
    print("\n1. Student registration")
    print("2. Faculty registration")
    print("3. Guest registration")
    print("4. Park Vehicle")
    print("5. Remove Vehicle")
    print("6. Exit")
    print("7. Check User ID Validity")
    print("8. Check Vehicle number Validity")
    choice = input("Enter your choice: ")

    if choice == "1":
        user_id = input("Enter User ID: ")
        vehicle_number = input("Enter Vehicle Number: ")
        valid_date = input("Enter Date of validation: ")
        parking.user_student(user_id, vehicle_number,valid_date)
    elif choice == "2":
        user_id = input("Enter User ID: ")
        vehicle_number = input("Enter Vehicle Number: ")
        valid_date = input("Enter Date of validation: ")
        parking.user_faculy(user_id, vehicle_number,valid_date)
    elif choice == "3":
        user_id = input("Enter User ID: ")
        vehicle_number = input("Enter Vehicle Number: ")
        valid_date = input("Enter Date of validation: ")
        parking.user_guest(user_id, vehicle_number,valid_date)
    elif choice == "4":
        user_id = input("Enter user ID: ")
        if parking.is_valid_user_id(user_id):
            parking.park_vehicle(user_id)
        else:
            print("Invalid User ID")
    elif choice == "5":
        user_id = input("Enter User ID: ")
        if parking.is_valid_user_id(user_id):
            parking.remove_vehicle(user_id)
        else:
            print("Invalid user ID")
    elif choice == "6":
        print("Exiting...")
        break
    elif choice == "7":
        user_id = input("Enter User ID: ")
        if parking.is_valid_user_id(user_id):
            print("Valid User ID")
            print(f"validity:{valid_date}") 
        else:
            print("Invalid user ID")
    elif choice == "8":
        vehicle_number = input("Enter vehicle number: ")
        if parking.is_valid_vehicle_number(vehicle_number):
            print("valid vehicle number")
            print(f"validity:{valid_date}")
        else:
            print("Invalid vehicle number")
    else:
        print("Invalid choice. Please try again.")
    
    
