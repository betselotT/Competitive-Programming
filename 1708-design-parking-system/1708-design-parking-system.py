class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.in_parking = [0, 0, 0]
        self.capacity = [big, medium, small]
    def addCar(self, carType: int) -> bool:
        carType -= 1
        if self.in_parking[carType] < self.capacity[carType]:
            self.in_parking[carType] += 1
            return True
        return False