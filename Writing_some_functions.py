import random

def find_min(numbers : list):
    """
    we wanna find the minimum element in a list
    """
    minimum = numbers[0]
    for i in range(1,len(numbers)):
        if minimum > numbers[i]:
            minimum = numbers[i]
    return minimum

def find_max(numbers: list):
    """
    we wanna find the maximum element in a list
    """
    maximum = numbers[0]
    for i in range(1, len(numbers)):
        if maximum < numbers[i]:
            maximum = numbers[i]
    return maximum

def concat_lists(l1:list, l2:list):
    """we will get 2 lists and add list1 to the end of list2"""
    concaninated = l2+l1
    return concaninated


def bubble_sort(l: list):
    """
    we will sort the list from lowest to highest
    """
    lengh = len(l)
    for i in range(lengh-1):
        for j in range(0, lengh-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l


def find_intersection(l1:list, l2:list):
    """
    we will find the intersection of two lists
    """
    intersections = []
    for item in l1:
        for element in l2:
            if item == element:
                    intersections.append(item)
    return intersections

def find_union(l1:list, l2:list):
    """
    we will find union of two lists
    """
    ejtema = l1 + l2
    union = []
    for item in ejtema:
        if item not in union:
            union.append(item)
    return union


len_list = int(input("Please enter the lenght of the list(n): "))
range_list = int(input("Please enter the range of the list(m): "))

list_1 = random.sample(range(range_list), len_list)
list_2 = random.sample(range(0,range_list),len_list)
print(list_1, list_2, sep="\n")

print("sorted list of the uninon of two list: ",bubble_sort(find_union(list_1,list_2)))  #print sorted list of the union
print("sorted list of the intersection of two list: ",bubble_sort(find_intersection(list_1,list_2))) #print sorted list of the intersection
print("sorted list of the concatenation of two list: ",bubble_sort(concat_lists(list_1,list_2))) #print sorted list of the concatenation
print("if both min are equal print True else print False: ",find_min(list_1) == find_min(list_2))
print("if both maximum are equal print True else print False: ",find_max(list_1) == find_max(list_2))
list_1.remove(find_min(list_1))  #removing the minimum from the list1
list_2.remove(find_min(list_2)) #removing the minimum from the list2
print(" the lists without minimum: ",list_1, list_2, sep= "\n") #printing the lists without minimum
list_1.remove(find_max(list_1)) #removing the maximum from the list1
list_2.remove(find_max(list_2)) #removing the maximum from the list2
print(" the lists without mmaximum: ",list_1, list_2, sep= "\n") #printing the lists without maximum