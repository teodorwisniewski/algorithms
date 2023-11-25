from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.check_in_map = dict() # id -> (stationName, time)
        self.summary_map = defaultdict(lambda: [0, 0]) # (startStation, endStation) -> [count, total]
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_map[id] = (stationName, t)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, start_time = self.check_in_map[id]
        route = (startStation, stationName)
        self.summary_map[route][0] += 1
        self.summary_map[route][1] += t - start_time
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        count, total = self.summary_map[(startStation, endStation)]
        return total/count


# Your UndergroundSystem object will be instantiated and called as such:
obj = UndergroundSystem()
id, stationName, t = 11, "Warsaw", 12
obj.checkIn(id, stationName, t)
id, stationName, t = 11, "Lodz", 14
obj.checkOut(id, stationName, t)
startStation, endStation = "Warsaw", "Lodz"
param_3 = obj.getAverageTime(startStation, endStation)
print(f"getAverageTime {param_3}")