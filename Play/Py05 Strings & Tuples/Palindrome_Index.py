"""
Write a Python function palindrome_index(s) that, given a string s, returns the index of the first character that, if removed, turns the string into a palindrome. If there is no such character or the string already is a palindrome, it should return -1. 
"""
def palindrome_index(s):
    if s == s[::-1]:
        return -1
    else:
        for i in range(len(s)):
            if s[:i] + s[i+1::] == (s[:i] + s[i+1::])[::-1]:
                return i
        return -1
