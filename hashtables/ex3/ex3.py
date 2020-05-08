def intersection(arrays):
    """
    YOUR CODE HERE
    """
    count = {}
    # list to results to
    result = []
    # iterate through our array with the index and array at index *use enumerate*
    for i, nums in enumerate(arrays):
        # iterate through individual arrays
        for j in nums:
            # if not our first array and key exists, increase count.
            if count.get(j) is not None and i > 0:
                count[j] = count[j] + 1
            # if first in array set each number in array to 1
            elif count.get(j) is None and i == 0:
                count[j] = 1
            # otherwise dont do anything
            else:
                continue
    
    # iterate through our dict
    for num in count:
        # check to see if count matches the amount of arrays checked and append it to our list
        if count[num] == len(arrays):
            result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
