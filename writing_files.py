# Writing into new file and appending the information into the existing files

employee_file_in_append_mode = open("employees.txt","a")

employee_file_in_append_mode.write("\nShivang-Software Developer")
print(employee_file_in_append_mode)

employee_file_in_append_mode.close()

employee_file_in_write_mode = open("employees.txt","w") # If the file exists, it will allow to override and if file doesn't exist then it will create a new file
employee_file_in_write_mode.write("\nShivang Suchak - Software Developer")
employee_file_in_write_mode.write("\nVishnu Venu - Kickass Angular Developer")

employee_file_in_write_mode.close()

index_file = open("index.html","w")

index_file.write("<p>This file is generated using a PYTHON Code</p>")
index_file.close()