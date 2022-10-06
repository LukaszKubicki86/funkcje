def isPalindrom(s):
    return s == s[::-1]

s = "kajak"
ans= isPalindrom(s)

if ans:
    print("yes")
else:
    print("no")