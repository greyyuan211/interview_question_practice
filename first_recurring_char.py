# //Google Question
# //Given an array = [2,5,1,2,3,5,1,2,4]:
# //It should return 2

# //Given an array = [2,1,1,2,3,5,1,2,4]:
# //It should return 1

# //Given an array = [2,3,4,5]:
# //It should return undefined

# Brute-force
def first_recurring_char(input):
  for i in range(0,len(input)):
    # use a hashtable to dealing with the following example:
    # //Given an array = [2,1,1,2,3,5,1,2,4]:
    # //It should return 1
    dict = {}
    for j in range(i+1,len(input)):
      if (input[j] in dict):
        return input[j]
      else:
        dict[input[j]] = j
      if (input[i]==input[j]):
        return input[i]
  return None

# hashtable O(n)
def first_recurring_char2(input):
  dict = {}
  for i in range(0,len(input)):
    if (input[i] in dict):
      return input[i]
    else:
      dict[input[i]] = i
  
# //Bonus... What if we had this:
# // [2,5,5,2,3,5,1,2,4]
# // return 5 because the pairs are before 2,2

print(first_recurring_char([2,5,1,2,3,5,1,2,4]))
print(first_recurring_char([2,1,1,2,3,5,1,2,4]))
print(first_recurring_char([2,3,4,5]))

print(first_recurring_char2([2,5,1,2,3,5,1,2,4]))
print(first_recurring_char2([2,1,1,2,3,5,1,2,4]))
print(first_recurring_char2([2,3,4,5]))
