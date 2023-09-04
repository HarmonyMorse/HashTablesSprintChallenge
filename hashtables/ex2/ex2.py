#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    flights = {}

    for tic in tickets:
        flights[tic.source] = tic.destination
    print(flights)

    current = "NONE"
    route = []
    for i in range(0, length):
        route.append(flights[current])
        current = flights[current]
    return route