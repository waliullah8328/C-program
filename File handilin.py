# File Handeling
file = open("C:/Users/User/text.txt", "a")
file.write("Welcome python class . It is very good time for me")
file.write("Hi This Ripon")
file.close()
read_file = open("C:/Users/User/text.txt", "r")
for i in read_file:
    print(i)