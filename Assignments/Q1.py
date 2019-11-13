# QUESTION 1
# Write a program that reads the contents of a file_in_read file. The program should create a dictionary in which the keys are the individual words found in the file and the values are the number of times each word appears. The program should either display the frequency of each word or create a second file containing a list of each word and its frequency

# SOLUTION

file=open('words.txt','w')
user_input=input('please input the words you want to type:')
file.write(user_input)
file.write('\n')

file.close()
file=open('words.txt','r')
file_in_read=file.read()
file_in_read=file_in_read.replace('\n',' ')
word_list=file_in_read.split(' ')
for word in word_list:
    word_1=''
    for i in range(len(word)):
        if word[i].isalpha():
            word_1+=word[i].lower()
    word_list[word_list.index(word)]=word_1
while '' in word_list:
    word_list.remove('')
dic={}
for word in word_list:
    if word not in dic:
        dic[word]=1
    else:
        dic[word]+=1

for word in dic:
    print(format(word),format(dic[word]))