from SortedTableMap import *

class FlightQuery(SortedTableMap):
    '''An application of SortedTableMap, used to query tickets of expeted period'''
    class Key:
        __slots__ = "_origin", "_dest", "_date", "_time"

        def __init__(self, origin, dest, date, time):
            self._origin = origin
            self._dest = dest
            self._date = date
            self._time = time
    
        def __lt__(self, other):
            if self._origin != other._origin:
                return self._origin < other._origin
            if self._dest != other._dest:
                return self._dest < other._dest
            if self._date != other._date:
                return self._date < other._date
            return self._time < other._time
    
        def __le__(self, other):
            if self._origin != other._origin:
                return self._origin <= other._origin
            if self._dest != other._dest:
                return self._dest <= other._dest
            if self._date != other._date:
                return self._date <= other._date
            return self._time <= other._time

        def __eq__ (self, other):
            return self._origin == other._origin and self._dest == other._dest and self._date == other._date and self._time == other._time
    
        def __str__(self):
            return "{0} : {1} : {2} : {3}".format(self._origin, self._dest, self._date, self._time)
    
        def __hash__(self):
            return hash((self._origin, self._dest, self._date, self._time))

        def to_tuple (self):
            return (self._origin, self._dest, self._date, self._time)
    
    def query (self, k1, k2):
        '''Return all the tickets of expected period with the same origin and destination'''
        k1 = self.Key(k1[0], k1[1], k1[2], k1[3])
        k2 = self.Key(k2[0], k2[1], k2[2], k2[3])

        if k1 > k2:
            return None
        else:
            result = []
            key, value = self.find_ge(k1)
            while key < k2:
                result.append((key.to_tuple(), value))
                key, value = self.find_gt(key)
            return result
    
    '''Adding an extra method that might be useful for the user'''
    def get_cheapest_ticket(self, k1, k2):

        tickets = self.query(k1, k2)
        if tickets == None:
            return None
        
        cheapest = tickets[0]
        for each in tickets:
            if each[1] < cheapest[1]:
                cheapest = each
        return cheapest
    

        
a = FlightQuery()
s = [("A", "B", 622, 1200, "No1"), ("A", "B", 622, 1230, "No2"), ("A", "B", 622, 1300, "No3")]
for each in s:
    key = a.Key(each[0], each[1], each[2], each[3])
    value = each[4]
    a[key] = value
print(len(a))

k1 = ("A", "B", 622, 1200)
k2 = ("A", "B", 622, 1300)
a.query(k1, k2)
a.get_cheapest_ticket(k1, k2)



