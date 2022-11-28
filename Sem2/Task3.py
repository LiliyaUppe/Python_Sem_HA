# 3. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

#variant1
# str1 = input()
# str2 = input()
# count1 = str1.count(str2)
# print(count1)

#variant2
# str1 = input()
# str2 = input()
# count = 0
# while str2 in str1:
#     str1 = str1.replace(str2, '',1)
#     count+=1
# print(count)


#variant3
# str1 = input()
# str2 = input()
# print(int((len(str1) - len(str1.replace(str2, '')))/len(str2)))

#variant4 (проверяем срез на соответствие)
a = input()
b = input()
count = 0
for i in range(len(a)):
    if a[i:i+len(b)] == b:
        count += 1
print(count)
print(a.count(b))
