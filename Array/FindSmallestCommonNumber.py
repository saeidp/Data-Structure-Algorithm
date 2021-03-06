# Given three integer arrays sorted in ascending order, find the smallest number that is common
# in all three arrays. For example, let's look at the below three arrays. 
# Here 6 is the smallest number that's common in all the arrays. [6,7,10], [5,6,7], [1,6,10, 14]

# Take advantage of the sorted array to reduce complexity.
# Use three pointers.
# O(n) , O(1)
def find_least_common_number(a,b,c):
  i=0
  j=0
  k=0

  while i < len(a) and j < len(b) and k < len(c):

    # Found the smallest common number
    if a[i] == b[j] and b[j] == c[k]:
      return a[i]

    # Let's advance the iterator
    # for the smallest value.

    if a[i] <= b[j] and a[i] <= c[k]:
      i+=1
    elif b[j] <= a[i] and b[j] <= c[k]:
      j+=1
    elif c[k] <= a[i] and c[k] <= b[j]:
      k+=1

  return -1

a = [6, 7, 10, 25, 30, 63, 64]
b = [-1, 4, 5, 6, 7, 8, 50]
c = [1, 6, 10, 14]
common = find_least_common_number(a,b,c)

print(common)