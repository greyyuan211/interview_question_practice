# Write a program to count the number of bit sets in a number
# O(logn)
def count_bit_set(numInput):
  count = 0
  while (numInput>0):
    count += numInput & 1
    numInput >>= 1
  return count

print(count_bit_set(9))
      