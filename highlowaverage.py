#For this assignment use the numbers.txt file.
#A different numbers.txt will be used for grading.
#Read in all the numbers. Display the following information:
#How many numbers in the file
#Total of all the number
#Average
#Highest number
#Lowest number
#Correct answers for the included file:

numberfile = open("numbers.txt", 'r')

count = 0
sum = 0
max = 0
min = 0




for curline in numberfile:
    num = int(curline)
    count += 1
    sum += num
    if count == 1:
        max = num
        min = num
    else:
        if num > max:
            max = num
        if num < min:
            min = num
    
print("The number of numbers is: ", count) 
print("The number is: ", sum)
print("The average is: ", sum/count)
print("The highest number is: ", max)
print("The lowest number is: ", min)
   