# 3. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

#variant1
# str1 = input()
# str2 = input()
# count1 = str1.count(str2)
# print(count1)

#variant2
str1 = input()
str2 = input()
count = 0
while str2 in str1:
    str1 = str1.replace(str2, '', 1)
    count += 1
print(count)
