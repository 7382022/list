l = [4,5,1,2,9,10,8]
print("original list:",l)

#variable to store the sum of
#the list
count = 0

#Finding the sum
for i in l:
    count += i

#divide the total elements by 
#number of elements
avg = count/len(l)

print("sum =", count)
print("average", avg)

# Sorting the elements of the list
l.sort()

#printing the first element
print("smallest element is:", l[0])

#printing the last element
print("Largest element is:", l[-1])