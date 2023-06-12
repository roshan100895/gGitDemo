file = open("text") # open the file to read or write

# read all the content of the file
# read n no of characters by passing parameter
#print(file.read(5))
#print(file.readline())
#print(file.readline())
#print(file.readline())
#print(file.readline())

# ---> Interview questionprint line line by line using readLine method <--
#line = file.readline()
#while line!= "":
   # print(line)
    #line = file.readline()

# read line will read all the line and store in the list
# values = [apple, banana, cat, dog, elephant]
for line in file.readlines():
    print(line)




file.close()