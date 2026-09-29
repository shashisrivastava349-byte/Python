#collections data types
#1. List : It is a collection which is ordered and changeable. Allows duplicate members.
# my_list = ["apple", "banana", "cherry"]
# print(my_list)
# print(type(my_list))

# list_index = [1,4,5,6,9]
# print(list_index[2])
# print(list_index[-1])
# print(list_index[-2])

# print("Length of list is :", len(list_index))
#
# for item in range(len(list_index)):
#     print(list_index[item])

# print("Before updating element :",list_index)
# list_index[2] = 10
# print("After updating element :",list_index)

# print("Before Append element :",list_index)
# list_index.append(15)
# print("After Append element :",list_index)

# print("Before insert element on index 2 :",list_index)
# list_index.insert(2, 10)
# print("After insert element on index 2 :",list_index)

# print("Before remove element :",list_index)
# list_index.remove(4)
# print("After remove element :",list_index)

# print("Before pop element :",list_index)
# list_index.pop()    # it will remove last element from list
# list_index.pop(2)       # it will remove element from index 2
# print("After pop element :",list_index)

# print(list_index.clear())

# print("Before reverse element :",list_index)
# list_index.reverse()
# print("After reverse element :",list_index)
#
# print("Before sort element :",list_index)
# list_index.sort()
# print("After sort element :",list_index)

# print(list_index.index(4))  # it will return index of element 4 in list

# nested_list=[1, 2, 3, [4, 5, 6], [7, 8, 9]]
# print(nested_list[3][1])  # Output: 5

# a=[1,2,3,4,5,5,6,7,5,8,9,10]
# # print(a[2:6])  # Output: [3, 4, 5, 6]
# # print(a[:2])
# # print(a[2:-5])
# # print(a[3:])
# print(a.count(5))
# print(max(a))
# print(min(a))
# print(sum(a))



#2. Tuple : It is a collection which is ordered and unchangeable. Allows duplicate members.
# my_tuple = ("apple", "banana", "cherry")
# print(my_tuple)
# print(type(my_tuple))

a=(9,2,4,5,6,)
# print(a[3])
# print(a[-3])

# for i in range(len(a)):
#     print(a[i])

# for j in a:
#     print(j)

# print(a[1:4])  # Output: (2, 4, 5)
# print(4 in a)  # Output: True
# print(10 not in a) # Output: True
# print(a.index(5))  # Output: 3

# nested_tuple = (1, 2, 3, (4, 5, 6), (7, 8, 9))
# print(nested_tuple[3][1])  # Output: 5


#3. Set : It is a collection which is unordered and unindexed. No duplicate members.
# my_set = {"apple", "banana", "cherry"}
# print(my_set)
# print(type(my_set))

# a={2,4,7,8,6,7,6}
# print(a)
# print(type(a))
# print(len(a))
# # a.add(5)
# a.update([1,3])
# #a.remove(3)
# print(a)

# for i in a:
#     print(i)

# print(7 in a)  # Output: True
# print(7 not in a)  # Output: False

# a={2,4,7,8,6,7,6}
# b={7,2,10,11,12,13}
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# print(a.symmetric_difference(b))
#
# print(max(a))
# print(min(a))
# print(sum(a))

#4. Dictionary : It is a collection which is ordered and changeable. No duplicate members.
my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
# print(my_dict)
# print(type(my_dict))

# print(my_dict["brand"])
# print(my_dict.get("model"))
# print(my_dict.keys())
# print(my_dict.values())
my_dict["color"] = "red"
# print(my_dict)

# for car in my_dict.keys():
#     print(car)
#
# for car in my_dict.values():
#     print(car)

# for car in my_dict.keys():
#     print(car, my_dict[car])

# for k, v in my_dict.items():
#     print(k, v)

# print(my_dict)
# my_dict.pop("brand")
# print(my_dict)

my_dict.popitem()  # it will remove last item from dictionary
print(my_dict)

print(len(my_dict))
















