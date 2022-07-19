"""
Build your own function to find common values of three lists using a set
"""

def intersect_lists(list_1, list_2, list_3):
    new_list = []

    # You can see that this function only goes through all of the data once, then does several O(1) operations

    set_2 = set(list_2)
    set_3 = set(list_3)

    for item in list_1:
        if item in set_2:
            if item in set_3:
                new_list.append(item)

    return new_list


list_1 = [2,3,5,6,8,9,10,12,13,21]
list_2 = [8,7,11,19,20,5,1,0,21,6,10]
list_3 = [5,6,11,17,10,20,8,21,14,4,13]

new_list = intersect_lists(list_1,list_2,list_3)
print(new_list) #Expected: [5, 6, 8, 10, 21]