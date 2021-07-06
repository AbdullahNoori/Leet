'''Write a Sort function to sort the elements in  a list WITHOUT using the list.sort function(descending order)'''


data_list = [100, 55, 44, 32, 2, 7, 8, 10, 3, 3, 4, 0, 1]


new_list = []


while data_list:
    minimum = data_list[0] #arbitrary number in list
    
    for x in data_list:
        if x > minimum:
            minimum = x
    
    new_list.append(minimum)
    data_list.remove(minimum)
    
print(new_list)