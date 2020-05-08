#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    trip_dict = {}
    # array to append destinations
    route = []
    # iterate through tickets
    for i in tickets:
        # add source and destination to dict
        trip_dict[i.source] = i.destination
    # set starting index
    index = 0
    # set starting source
    cur_dest = "NONE"
    # iterate through list until index matches length
    while index < length:
        # get the destination of our current source and set it as our current destination
        cur_dest = trip_dict.get(cur_dest)
        # append it to our list
        route.append(cur_dest)
        # increase index
        index += 1

    return route
