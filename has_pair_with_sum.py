#[1,2,3,9] sum=8 no
#[1,2,4,4] sum=8 yes
# input: arr sum
# output: bool

arr1 = [1,2,3,9]
arr2 = [1,2,4,4]

#O(n)
def hasPairWithSum(arr, sum):
  lo = 0;
  hi = len(arr)-1;
  while (lo<hi):
    s = arr[lo]+arr[hi]
    if (s==sum):
      return True
    else:
      if (s<sum):
        lo+=1
      if (s>sum):
        hi-=1
  return False;

# no longer given a sorted array (HashSet)
def hasPairWithSum2(arr, sum):
  comp = set([])
  for i in arr:
    diff = sum - i
    print(diff)
    if (diff in comp):
      return True
    comp.add(diff)
  return False
    


print(hasPairWithSum2(arr2,8))