# reverse a string

# using built-in reverse array function
def reverse1(str):
  return ''.join(reversed(list(str)))

# self coded the reversed() function
def reverse2(str):
  reversed_str = []
  str_list = list(str)
  for i in reversed(str_list):
    reversed_str.append(i)
  return ''.join(reversed_str)

# using built-in reverse string function
def reverse3(str):
  return ''.join(reversed(str))

# using slicing string
def reverse4(str):
  return str[::-1]

# using slicing array
def reverse5(str):
  return ''.join(list(str)[::-1])

print(reverse1('Hi Linwei! Keep on practicing!'))
print(reverse2('Hi Linwei! Keep on practicing!'))
print(reverse3('Hi Linwei! Keep on practicing!'))
print(reverse4('Hi Linwei! Keep on practicing!'))
print(reverse5('Hi Linwei! Keep on practicing!'))