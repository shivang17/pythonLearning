employee_file = open("employees.txt","r") 

# The second parameter determines the mode in which you want the file to be open. Here, r is for read, you can't do any other operations

# "w" is for write mode
# "a" is for append mode, You can't modify anything in the file but you can append your information to the file

# "r+" is for read and write


# Before printing or doing any function on the file, make sure to check whether the file is readable or not in the read mode
print(employee_file.readable()) # Should return true if the mode mentioned is "r"

# print(employee_file.read()) # Reads the entire file

print(employee_file.readlines()) # readlines will convert each line into a list
employee_file.close()

map_file = open("map.txt","r")

map_file_read = map_file.readlines()

for line in map_file_read:
    print(line)