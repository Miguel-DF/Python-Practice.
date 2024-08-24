
# variable type can set text in text file
text = input("Write a message :")

# with open can write the variable data type with name of text and 'w' is write
with open('test.txt','w') as file:
    file.write(text)
    print("Writing in File is SUccesfully!")

