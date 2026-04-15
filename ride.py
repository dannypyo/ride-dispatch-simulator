import random
import time

# ***************** SAMPLE DATA
rider_names = ["Alice", "John", "Maria", "Ethan", "Zara", "Leo"]
locations = ["Union Station", "5th Ave", "Central Park", "16th Street", "Denver Tech Center", "Broadway"]

# ***************** GENERATE RIDE
def generate_rides():
    ride_id = 1
    while True:
        rider = random.choice(rider_names)
        pickup = random.choice(locations)
        destination = random.choice([loc for loc in locations if loc != pickup])
        yield {
            'ride_id': f"R{ride_id:03d}",
            'rider_name': rider,
            'pickup': pickup,
            'destination': destination
        }
        ride_id += 1
        time.sleep(random.uniform(0.5,1.5))

# ***************** DRIVERS
def driver_pool():
    drivers = [
        {"driver_id": "D001", "name": "Bob", "current_status": "available"},
        {"driver_id": "D002", "name": "Tina", "current_status": "available"},
        {"driver_id": "D003", "name": "Raj", "current_status": "available"},
    ]
    
    while True:
        for driver in drivers:
            if driver["current_status"] == "available":
                yield driver

# ***************** DISPATCH RIDES
def dispatch_loop():
    ride_generator = generate_rides()
    available_drivers = driver_pool()
    
    completed_rides = 0
    max_rides = 5

    print("\n===  RideNow Dispatch System Simulation ===\n")

    while completed_rides < max_rides:
        ride = next(ride_generator)
        driver = next(available_drivers)

        print(f"\nRide Request: {ride['rider_name']} from {ride['pickup']} to {ride['destination']}")
        print(f"→ Assigned to Driver: {driver['name']} ({driver['driver_id']})")

        driver["current_status"] = "on_ride"

        print(f"→ {driver['name']} is picking up {ride['rider_name']}...")
        time.sleep(1)
        print(f"→ {driver['name']} is en route to {ride['destination']}...")
        time.sleep(1)
        print(f"→ {driver['name']} has dropped off {ride['rider_name']} at {ride['destination']}.")
        
        driver["current_status"] = "available"
        print(f"→ {driver['name']} is now available again.")

        completed_rides += 1

    print(f"\n Simulation completed: {completed_rides} rides dispatched.")

if __name__ == "__main__":
    dispatch_loop()