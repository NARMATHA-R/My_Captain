filename = input("Input the Filename: ")
extns = filename.split(".") # split()- Splits the string at the specified separator, and returns a list
print ("The extension of the file is : " ,extns[-1])# -1 indicates the last element in a sequence

#OUTPUT
Input the Filename: abc.python
The extension of the file is :  python
