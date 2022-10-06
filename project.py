from re import S


def isPalindrom(s):
    return s == s[::-1]

s = input("podaj slowo zobaczymy czy jest to palindrom:")
ans= isPalindrom(s)
print(bool(ans))
