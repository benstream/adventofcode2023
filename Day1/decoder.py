# decorder.py
# The Elves are going to shoot me on a trebuche I need the correct decoded inputer (sum of all terms)
# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
# For example:
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.
# Consider your entire calibration document. What is the sum of all of the calibration values?

sumdigits = 0
with open(".\Day1\input.txt","r") as txt:
    for line in txt:
       digits = list(filter(lambda i: i.isdigit(), line))
       sumdigits += int(str(digits[0])+str(digits[-1]))
    print("Your sum is: " + str(sumdigits))

       