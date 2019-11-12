                        # QUESTION 10   

# Write a program that lets the user enter a string (a sentence) and displays the character that appears most frequently in the string

str = input("Enter the string")
ascii_size = 256
def most_frequent_character(str): 
    count = [0] * ascii_size 
  
    max = -1
    character = '' 
  
    for i in str: 
        count[ord(i)]+=1; 
  
    for i in str: 
        if max < count[ord(i)]: 
            max = count[ord(i)] 
            character = i 
  
    return character

print(most_frequent_character(str))
# ASSUMPTION: The characters are case sensitive