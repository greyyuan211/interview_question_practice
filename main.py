# Given an interger X, find the number of intergers less than or equals to X whose digits adds up to Y
# Input X=20 Y=5 Output 2

# O(n^2)
def solution(X,Y):
  result = 0
  for i in range(1,X+1):
    sum_i = sum(int(x) for x in str(i)) #return a list of sums of digits
    if sum_i==Y:
      result = result+1 
  return result;

print(solution(20,1))
print(solution(20,5))
print(solution(20,0))
print(solution(1000,1))