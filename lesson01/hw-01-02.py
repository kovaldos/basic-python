# 2-Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. Предикату можно заменить на понятие "бит".
# Должна получиться таблица истинности.


print("x y z f")
for x in range(2):
	for y in range(2):
		for z in range(2):
			if (not(x or y or z)) == (((not x) and (not y)) and (not z))==1:
				print(x, y, z, 1)
			else:
				print(x, y, z, 0)