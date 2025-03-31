#For this assignment use the words.txt file.
#Read in all the words. Count how many are palindromes, or words that are spelled the same forwads and backwards.
#For example, wow is a paldindrome.
#A different file wile be used for grading.
#Correct answer for this file: 

wordfile = open("words.txt", 'r')
counter = 0

file = wordfile.read().splitlines()



for word in file:
    if word == word[::-1]:
        counter += 1
        
    else:
        counter += 0
        

print("This is the number of palindromes in the file: ",  counter)
        