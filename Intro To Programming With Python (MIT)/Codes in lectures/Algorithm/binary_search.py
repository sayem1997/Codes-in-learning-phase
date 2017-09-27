def binary_search(list, search):
    length = len(list)
    guess = int(length/2)
    while list[guess] != search and 0<=guess<=(length-1):
