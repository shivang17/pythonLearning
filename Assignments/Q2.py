# QUESTION 2
# Write a program that reads the contents of a text file. The program should create a dictionary in which the key-value pairs are described as follows:


# Key: The keys are an individual word found in the file
 	
# Values: Each value is a list that contains the line numbers in the file where the word is found
# For example: if a word says ‘robot’ appears inline 7, 8, 23, and 45, then the dictionary should have the format: Key: value = ‘robot’ : [7, 8, 23, 45]. Once done, store the dictionary in a file

file=open('words.txt','w')


user_input=input('please input the words you want to type:')
file.write(user_input)
file.write('\n')
file.close()
file=open('words.txt','r')
dic={}
line_number=0
for line in user_input:
    line_number+=1
    word_list=line.rstrip('\n').split(" ")
    for word in word_list:
        if word in dic:
            wordlist=dic[word]
            wordlist.append(line_number)
            dic[word]=wordlist 
        else:
            wordlist=[line_number]
            dic[word]=wordlist

opt_file=open('assignment_2.txt','w')
for i in sorted(dic.keys()):
    opt_file.write(str(i)+":")
    for j in range(len(dic[i])):
        opt_file.write(str(dic[i][j])+', ')
    opt_file.write('\n')
opt_file.close()
print('Content added to the file') 