# Дан список, вывести отдельно буквы и цифры
a = ('a', 'b', '2', '3', 'c', '4', '5')
b = ('a', 'b', 'c')
c = ('1', '2', '3')

b= filter(str.isalpha, a)
с= filter(str.isdigit, a)

print(*b)
print(*c)