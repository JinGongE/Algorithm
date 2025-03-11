str1 = "1"+input()
str2 = "1"+input()

arr = [[0 for _ in range(len(str2))] for _ in range(len(str1))]

for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        if str1[i] == str2[j]:
            arr[i][j] = arr[i-1][j-1]+1
        else:
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])
    
print(arr[len(str1)-1][len(str2)-1])
