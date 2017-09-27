def avrg_of_list(list):
    assert len(list) != 0, 'No data to get average'
    return sum(list)/len(list)

print(avrg_of_list([1,2,32]))