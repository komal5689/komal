# Open a File on the Server
f = open("file.txt", "r")
print(f.read())

'''0/p
Hello world!
Hello world!
Hello world!
Hello world!'''

# Read Only Parts of the File
f = open("file.txt", "r")
print(f.read(5))

'''o/p
Hello'''

# Read one line by using the readline()
f = open("file.txt", "r")
print(f.readline())

'''o/p
Hello world!'''


# Open the file "demofile2.txt" and append content to the file:
f = open("file2.txt", "a")
f.write("Now the file has more content+!")
f.close()

#open and read the file after the appending:
f = open("file2.txt", "r")
print(f.read())

# '''''''''''''

# Open the file "file3.txt" and overwrite the content:
f = open("file.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("file.txt", "r")
print(f.read())
