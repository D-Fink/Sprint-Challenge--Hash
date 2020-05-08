def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    weight_dict = {}

    #iterate through the length of weights
    for i in range(length):
        #calculate if current weight matches remainder of any weights in dict
        calc = weight_dict.get(limit - weights[i])
        # if calculate finds match, return the indexes
        if calc is not None:
            return (i, calc)
        #if calculate returns none, assign weight an index and add to dict
        else:
            weight_dict[weights[i]] = i

    return None
