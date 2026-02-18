str1, str2 = "silent", "listen"

if sorted(list(str1)) == sorted(list(str2)):
    print(f"{str1} and {str2} are anagram strings")
else:
    print(f"{str1} and {str2} are not anagram strings")