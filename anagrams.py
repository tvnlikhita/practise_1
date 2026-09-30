s1, s2 = "silent", "listen"

if sorted(list(s1)) == sorted(list(s2)):
    print(f"{s1} and {s2} are anagram strings")
else:
    print(f"{s1} and {s2} are not anagrams")