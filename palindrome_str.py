str1 = "malayalam"
m = len(str1)//2
cnt = 0

for i in range(m):
    if str1[i] == str1[len(str1)-1-i]:
        cnt += 1
if cnt == m:
    print(f"{str1} is palindrome string")
else:
    print(f"{str1} is not a palindrome string")