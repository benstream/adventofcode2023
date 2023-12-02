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

# OG VERSION! Doesnt cound spelled out numbers as numbers! Now we need to...
# sumdigits = 0
# with open(".\Day1\input.txt","r") as txt:
#     for line in txt:
#        digits = list(filter(lambda i: i.isdigit(), line))
#        sumdigits += int(str(digits[0])+str(digits[-1]))
#     print("Your sum is: " + str(sumdigits))

# You need to fill in letter replaced to allow for numbers edged on eachother
# ie :: eightwo 
numdict = {
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e',
}

def multipleReplace(text, wordDict):
    for key in wordDict:
        text = text.replace(key, wordDict[key])
    return text

string1 = "ninexskpsth5sevennine"
new_string = multipleReplace(string1,numdict)
print(new_string)
def sumStringNum(path):
    sumdigits = 0
    with open(path,"r") as txt:
        for line in txt:
            line_numbered = line# multipleReplace(line,numdict)
            #print(line_numbered)
            digits = list(filter(lambda i: i.isdigit(), line_numbered))
            #print(digits)
            sumdigits += int(str(digits[0])+str(digits[-1]))
        print("Your sum is: " + str(sumdigits))

def sumStringAlphaNum(path):
    sumdigits = 0
    with open(path,"r") as txt:
        for line in txt:
            line_numbered = multipleReplace(line,numdict)
            print(line_numbered)
            digits = list(filter(lambda i: i.isdigit(), line_numbered))
            print(digits)
            sumdigits += int(str(digits[0])+str(digits[-1]))
        print("Your sum is: " + str(sumdigits))

sumStringNum(".\Day1\\test1.txt")

sumStringAlphaNum(".\Day1\\test2.txt")
sumStringNum(".\Day1\input.txt")
sumStringAlphaNum(".\Day1\input.txt")