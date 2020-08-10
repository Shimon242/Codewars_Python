# You are going to be given a word. 
# Your job is to return the middle character of the word. 
# If the word's length is odd, return the middle character. 
# If the word's length is even, return the middle 2 characters.

def get_middle(s):
    #your code here
    num = len(s)
    if num % 2 == 0:
        slot1 = num // 2
        slot2 = num // 2 - 1
        middle1 = s[slot1]
        middle2 = s[slot2]
        return (str(middle2 + middle1))
    else:
        slot = num // 2
        middle = s[slot]
        return (middle)

# Sample Tests

Test.assert_equals(get_middle("test"),"es")
Test.assert_equals(get_middle("testing"),"t")
Test.assert_equals(get_middle("middle"),"dd")
Test.assert_equals(get_middle("A"),"A")
Test.assert_equals(get_middle("of"),"of")
