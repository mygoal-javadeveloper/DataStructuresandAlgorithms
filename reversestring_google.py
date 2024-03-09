"""This problem was asked by Google.

Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here",
return "here world hello"

Follow-up: given a mutable string representation, can you perform this operation in-place?

"""

def reversestring(mystr:str) -> str:
    mystr = mystr.strip().split()
    mystr.reverse()
    return ' '.join(mystr)


print(reversestring("hello world here"))
