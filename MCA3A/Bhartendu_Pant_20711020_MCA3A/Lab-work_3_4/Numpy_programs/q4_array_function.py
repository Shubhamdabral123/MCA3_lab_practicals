list = ['c','java','js','python','c']
print("list is:",list)
#Use of append method

list.append("JS")
print("After using append list is:",list)

#use of count method

x = list.count("c")
print("count of C in list is:",x)

#use of index method
y = list.index("python")
print("index of python in list is:",y)

#use of reverse method
list.reverse()
print("After reversing the list:",list)

#use of pop method
list.pop()
print("Array after poping element from the list",list)
