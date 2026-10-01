#file handling in python

#open a file
file = open("D:\\Python\\PracticePythonFolder\\Files\\shashi.txt", "w") #open a file in write mode
file.write("Hello World\n") #write to the file
file.write("This is a test file\n") #write to the file
file.close() #close the file

# open a file
file = open("D:\\Python\\PracticePythonFolder\\Files\\shashi.txt", "r") #open a file in read mode
# content = file.read() #read the file
# print(file.readline())
content = file.readlines()
for line in content:
    print(line.strip()) #print the content of the file
# print(content) #print the content of the file
file.close() #close the file

file=open("D:\\Python\\PracticePythonFolder\\Files\\shashi.txt", "a") #open a file in append mode
file.write("This is an appended line\n") #append to the file
file.close() #close the file