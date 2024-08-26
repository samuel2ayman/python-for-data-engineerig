class vehicle:
    color="white"
    def __init__(self,max_speed,mileage):
       self.max_speed=max_speed
       self.mileage=mileage
       
    def assign_seating_capacity(self,seating_capacity):
       self.seating_capacity=seating_capacity
    
    def display_properties(self):
        print("properties of vehicle")
        print(f"max speed {self.max_speed}")
        print(f"mileage {self.mileage}")
        print(f"seating capacity {self.seating_capacity}")

v1=vehicle(200,20)
v1.assign_seating_capacity(5)
v1.display_properties()

v2=vehicle(180,25)
v2.assign_seating_capacity(4)
v2.display_properties()