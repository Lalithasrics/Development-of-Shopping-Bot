file = open("myfile.txt", "r")
content = file.read()
print(content)
Counter=0
CoList = content.split("\n")
 
for i in CoList:
    if i:
        Counter += 1
 
print("This is the number of lines in the file")
print(Counter)
file.close()
tr=content.find('Hide & Sick Biscuit')
if(tr>=0):
    print('product Picked')
    file_to_delete = open("myfile.txt",'w')
    file_to_delete.close()
else:
    print("no item")
    
    
