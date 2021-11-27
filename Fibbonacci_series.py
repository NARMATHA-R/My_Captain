#Python program to generate Fibonacci series until 'n' value
n = int(input("Enter the value of 'n': "))
a = 0
b = 1
sum = 0
count = 1 # just a variable to count the sequence of fibonacci series
print("Fibonacci Series: ",sum)
while(count <= n):
  print(sum)
  count += 1
  a = b
  b = sum
  sum = a + b
  
  #OUTPUT
 Enter the value of 'n': 10
Fibonacci Series:  0
0
1
1
2
3
5
8
13
21
34
