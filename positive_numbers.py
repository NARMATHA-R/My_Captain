#1st program
list1 = [12,-7,5,64,-14]
for number in list1:
    if number >=0:
        print(number,end =' ')# the end=' ' is used to place a space after value instead of a newline.
        
#output:12 5 64 

#2nd program
list2 = [12,14,-95,3]
positive_list = [number for number in list2 if number >=0]
print(positive_list)
        
#output:[12, 14, 3] 
