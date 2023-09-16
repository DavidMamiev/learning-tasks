array = input('введите список').split()
array = [int(i) for i in array]
new_array = []
def min_sorter(list, newlist):
    min = list[0]
    for i in range(len(list)-1):
        if min > list[i+1]:
            min = list[i+1]
    list.remove(min)
    newlist.append(min)
    return list, newlist
while len(array) != 0:
    array, new_array = min_sorter(array, new_array)
print(new_array)