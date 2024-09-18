file = open("my_file.txt", "w+")
file.write("The sum of two numbers; 2 and 5 is equal to 5.")

file.seek(0)
data = file.read()
# print(data)

file = open("my_file.txt","a+")
file.write("\nThe above statement is false.")


file.seek(0)
print(file.read())




