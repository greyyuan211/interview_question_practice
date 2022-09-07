# mean: sum of numbers devided by N
# mode: most frequent number
# output both the mean and mode of the given array


def get_mode(inputArr,inputArr_size):
  freq = {} #dict to keep track of frequency of each number
  for i in inputArr:
    freq.setdefault(i,0)
    freq[i] += 1
  highest_freq = max(freq.values())
  return freq[highest_freq]

def get_mean(inputArr,inputArr_size):
  total = 0
  for i in inputArr:
    total += i
  return total/inputArr_size

inputArr = [1,2,3,4,2,2,3,4]
inputArr_size = len(inputArr)
print(get_mode(inputArr,inputArr_size))
print(get_mean(inputArr,inputArr_size))
print("-------------------------------")

inputArr = [1,2,7,3,2]
inputArr_size = len(inputArr)
print(get_mode(inputArr,inputArr_size))
print(get_mean(inputArr,inputArr_size))   