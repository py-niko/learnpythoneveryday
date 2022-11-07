m = 'Строка текста'
count = 0

for i in m:
    if i == "т":
        continue
        print('в строке есть буква т')
        count += 1
    print(i)

else:
    print('цикл завершён, букв т =', count)
