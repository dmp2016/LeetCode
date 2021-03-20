from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.data_cards = dict()
        self.data_time = defaultdict(dict)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.data_cards[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        from_station, t1 = self.data_cards[id]
        if from_station in self.data_time:
            p = self.data_time[from_station].set_default(stationName, [0, 0])
        else:
            p = self.data_time[from_station].set_default(stationName, [0, 0])
        p[0] += 1
        p[1] += t - t1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if startStation in self.data_time:
            p = self.data_time[startStation][endStation]
        else:
            p = self.data_time[endStation][startStation]
        return p[1] / p[0]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)