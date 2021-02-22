values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)

filename = input("Input the Filename: ")
f_extns = filename.split(".")
print("The extension of the file is : " + repr(f_extns[-1]))