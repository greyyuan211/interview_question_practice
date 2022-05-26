# merge two sorted arrays

# use python built-in sort function O(nlogm) using a special version of merge sort called Timsort
def mergeSortedArrays(arr1,arr2):
  arr3=arr1+arr2
  return sorted(arr3)


# O(n+m)
def mergeSortedArrays2(arr1,arr2):
  merged_arr = []
  arr1_item = arr1[0]
  arr2_item = arr2[0]
  i=1 #index of arr1: starting from 1 because 0 is in arr1_item
  j=1 #index of arr2

  #check easy cases
  if (len(arr1)==0):
    return arr2
  if (len(arr2)==0):
    return arr1

  while(arr1_item or arr2_item):
    # print(i,j)
    # print(merged_arr)
    # print('compare', arr1_item,arr2_item)
    if (arr2_item == None or arr1_item<arr2_item):
      merged_arr.append(arr1_item)
      if i > len(arr1)-1:
        arr1_item = None
      else:
        arr1_item = arr1[i]
      i+=1
    else:
      merged_arr.append(arr2_item)
      if j > len(arr2)-1:
        arr2_item = None
      else:
        arr2_item = arr2[j]
      j+=1
      
  return merged_arr

print(mergeSortedArrays([0,3,4,31], [3,4,6,30]))
print(mergeSortedArrays2([0,3,4,31], [3,4,6,30]))