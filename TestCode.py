# this program converts kilometers to miles and miles to kilometers.

# print()

# kilometers = 12.25
# miles = 7.38

# miles_to_kilometers = miles * 1.61
# kilometers_to_miles = kilometers / 1.61

# print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
# print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

# print()





# this program converts euros to dollars and ollars to euros

# euros = 100.25
# dollars = 92.50

# euros_to_dollars = euros * 1.09
# dollars_to_euros = dollars / 1.09

# print(euros, "euros is", round(euros_to_dollars, 2), "dollars")
# print(dollars, "dollars is", round(dollars_to_euros, 2), "euros")

# print()




# this program computes the number of seconds in a given number of hours

# hours = 2
# seconds_in_hour = 3600

# print("Hours: ", hours)
# print("Seconds in Hours: ", hours * seconds_in_hour)




"""
Scenario
Your task is to prepare a simple code able to evaluate the end time of a period of time, given as a number of minutes (it could be arbitrarily large). The start time is given as a pair of hours (0..23) and minutes (0..59). The result has to be printed to the console.

For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.

Don't worry about any imperfections in your code - it's okay if it accepts an invalid time - the most important thing is that the code produce valid results for valid input data.

Test your code carefully. Hint: using the % operator may be the key to success.

Test Data
Sample input:
12
17
59

Expected output: 13:16


Sample input:
23
58
642

Expected output: 10:40


Sample input:
0
1
2939

Expected output: 1:0

"""


# number_1 = input("enter a number: ")
# number_2 = input("Enter a second number: ")
# number_3 = input("Enter a third number: ")

# max_number = max(number_1, number_2, number_3)  # we can use the min() to return the lowest number

# print("The largest number is ", max_number)




import time

for i in range(1, 6):
    print (i, " Missisipi")
    time.sleep(1)

print("Ready or not, here I come!")

# Write a for loop that counts to five.
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    # Body of the loop - use: time.sleep(1)

# Write a print function with the final message.






print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
secret_number = 777
number = int(input("Enter a number: "))

if secret_number == number:
        print(number)
else:
    while number != secret_number:
        print("Ha ha! You're stuck in my loop!")
        int(input("Enter a number again:"))
        
        if secret_number == number:
            break
    
        
print("Well done, muggle! You are free now.")
            