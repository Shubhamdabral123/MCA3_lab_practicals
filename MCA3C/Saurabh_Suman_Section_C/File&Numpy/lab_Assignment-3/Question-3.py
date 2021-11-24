# Write a program to demonstrate the usage of file handling in Python.


# Creating the file and opening in the write mode.
file1 = open("D:/python/ClassRoomCode/Lab_Assignment_3/FirstFile.txt", "w")

txt = "My name is Saurabh Suman. "
file1.write(txt)

# Closing the file
file1.close()

# opening the file in the reading mode.
file1 = open("D:/python/ClassRoomCode/Lab_Assignment_3/FirstFile.txt", "r")
content = file1.read()
print(content)

file1.close()

# opening thee file in the append mode.
file1 = open("D:/python/ClassRoomCode/Lab_Assignment_3/FirstFile.txt", "a")
txt2 = "\nCurrently I am studying in the GEHU.\nI am perusing MCA."
file1.write(txt2)
file1.close()

# reading the whole file using loop.
file1 = open("D:/python/ClassRoomCode/Lab_Assignment_3/FirstFile.txt", "r")
print("----------------------------------------------------")
for line in file1:
    print(line)
file1.close()

# counting the no of line in the file.

file1 = open("D:/python/ClassRoomCode/Lab_Assignment_3/FirstFile.txt", "r")
linecount = 0
word = []
wordcount = 0
char = []
charCount = 0
for line in file1:
    linecount += 1
    word = line.split(" ")
    wordcount += len(word)
    for i in word:
        charCount += len(i)

print("-----------------------------------------------------")
print("Number of line in a file: ")
print(linecount)
print("Number of word in a file: ")
print(wordcount)
print("Number of character in a file: ")
print(charCount)

# -----------------OUTPUT---------------------------

# My name is Saurabh Suman.
# ----------------------------------------------------
# My name is Saurabh Suman.

# Currently I am studying in the GEHU.

# I am perusing MCA.
# -----------------------------------------------------
# Number of line in a file:
# 3
# Number of word in a file:
# 17
# Number of character in a file:
# 68
