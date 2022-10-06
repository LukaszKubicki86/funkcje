def isPalindrom(s):
    return s == s[::-1]

s = input("podaj slowo zobaczymy czy jest to palindrom:")
ans= isPalindrom(s)

if ans:
    print("yes")
else:
    print("no")