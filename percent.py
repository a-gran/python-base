connect = True;

while connect == True:
	number = input('Число: ')
	percent = input('Процент: ')
	while type(number) != int:
		try:
			number = int(number)
			percent = int(percent)
   
		except ValueError:
			print('Вводи целочисленные значения!')
			number = input('Число: ')
			percent = input('Процент: ')
   
	while type(percent) != int:
		try:
			number = float(number)
			percent = float(percent)

		except ValueError:
			print('Вводи целочисленные значения!')
			number = input('Число: ')
			percent = input('Процент: ')
   
	result = number / 100 * percent
 
	print('Ваш ответ: ', float(result))