def is_palindrome(str):
    temp = str.lower()
    newstr = ""
    for c in temp:
        if c.isalnum():
            newstr += c
    reversestr = newstr[::-1]

    if newstr == reversestr:
     return True 
    else:
      return False
teststr = "Madam, I'm Adam"
answer = is_palindrome(teststr)
print(answer)   