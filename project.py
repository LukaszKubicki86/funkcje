from re import S


def isPalindrom(s):
    return s == s[::-1]  #odczytanie co któregoś elementu listy w tym wypadku co 1 
# sprawdzanie czy slowo jest palindromem
s = input("podaj slowo zobaczymy czy jest to palindrom:")
ans= isPalindrom(s)
print(bool(ans))
