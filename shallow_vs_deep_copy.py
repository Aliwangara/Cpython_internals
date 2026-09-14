# we have: =,copy(),deepcopy()

lst1 = [1,2,3,4,5,6]
lst2 = lst1
print(lst1)#[1, 2, 3, 4, 5, 6]

lst2[1] = 100
print (lst1,lst1) # [1, 100, 3, 4, 5, 6]
# this works because ls1 and ls2 both point to same memory location


# copy() also known as shallow copy

list1 = [1,2,3,4,5,6]
list2 = list1.copy()

list2[1] = 200
print(list2,list1) # [1, 200, 3, 4, 5, 6] [1, 2, 3, 4, 5, 6]

#This shows different output because when we copy this creates a different memory location from list 1 so a 
# new memory location is created for list2

# nested list using shallow copy

nstlist_1 = [[1,2,3,4],[5,6,7,8]]
nstlist2 = nstlist_1.copy()

nstlist_1[0][2] = 300

print(nstlist_1,nstlist2) # [[1, 2, 300, 4], [5, 6, 7, 8]] [[1, 2, 300, 4], [5, 6, 7, 8]]

# shallow copy duplicates the outer container, but the items inside are still shared references,
#  not independent copies  it copies "one layer deep" only
# #because if I use .append for list 1 and add something like [9, 10, 11, 12] this changes for list1 and not 2


# deepcopy()

import copy

dp_lis1 = [1,2,3,4,5]
dp_list_2 = copy.deepcopy(dp_lis1)
print(dp_list_2)

#in a list that is single dimension(normal list) deep copy works same as shallow copy 

# for nested deep copy

nst_dpcopy1 = [[1,2,3,4,5],[6,7,8,9],[10,11,12,13]]
nst_dpcopy2 = copy.deepcopy(nst_dpcopy1)

nst_dpcopy2[1][0] = 600
print(nst_dpcopy1,nst_dpcopy2)# [[1, 2, 3, 4, 5], [6, 7, 8, 9], [10, 11, 12, 13]] [[1, 2, 3, 4, 5], [600, 7, 8, 9], [10, 11, 12, 13]]

# with a deep copy this creates a new memory location reason why a specific object is changed unlike shallow copy
