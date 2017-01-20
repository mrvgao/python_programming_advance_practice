# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

def is_palindrom(text):
    text = text.replace(' ', '').lower()
    for i in range(len(text)/2):
        if text[i] != text[-(1+i)]:
            return False
    else:
        return True


def bruce_subpalindrome(text):
    begin, end = 0, 0
    #for begin in range(text)

    
def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # Your code here
    

def test_is_palindrom():
    L = is_palindrom
    assert(L('racecar') == True)
    assert(L('Racecar') == True)
    assert(L('Race car') == True)
    assert(L('RaceDcar') == False)
    print('test done!')


def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

#print test()
print test_is_palindrom()
