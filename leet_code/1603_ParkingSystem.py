




class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.car_spots = [big, medium, small]
        
    def addCar(self, carType: int) -> bool:

        if self.car_spots[carType-1] > 0:
            self.car_spots[carType-1] -= 1
            return True
        else:
            return False
        


parkingSystem = ParkingSystem(1, 1, 0)
responses = []
for input in [1, 2, 3, 1]:
    res = parkingSystem.addCar(input)
    responses.append(res)
print(responses)