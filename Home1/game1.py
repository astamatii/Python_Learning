import os
import msvcrt
os.system('cls')
print('УГАДАЙ ЗАГАДКУ\n')
i=0
while i<3:
	a=input('По горам, по долам ходит шуба да кафтан.\n')
	if  a in ['Овца','овца']:
		print("Молодец! Овца\n\nнажми кнопку")
		msvcrt.getch()
		os.system('cls')
		break
	elif i<2:
		print('\nПодумай еще!\n\nнажми кнопку')
		msvcrt.getch()
		os.system('cls')
		i=i+1
		continue
	else:
		a=input('\nНе угадал :)) \nСдаешся? ')
		if a in ['yes','y','да','д','угу']: 
			print('эхх ты... Овца!\n\nнажми кнопку')  
			msvcrt.getch()
			os.system('cls')
			break
		else: 
			os.system('cls') 
			i=0

os.system('cls')
print('СЛЕДУЮЩАЯ ЗАГАДКА\n')
i=0
while i<3:
	a=input('Явился в жёлтой шубке:-Прощайте, две скорлупки!\n')
	if  a in ["Цыплёнок",'Цыпленок',"цыплёнок",'цыпленок']:
		print("Правильно! Цыплёнок\n\nнажми кнопку")
		msvcrt.getch()
		break
	elif i<2:
		print('\nПодумай еще!\n\nнажми кнопку')
		msvcrt.getch()
		os.system('cls')
		i=i+1
		continue
	else:
		a=input('\nНе угадал :)) \nСдаешся? ')
		if a in ['yes','y','да','д','угу']: 
			print('эхх ты... Цыплёнок!\n\nнажми кнопку') 
			msvcrt.getch()
			os.system('cls')
			break
		else: i=0

os.system('cls')
print('СЛЕДУЮЩАЯ ЗАГАДКА\n')
i=0
while i<3:
	a=input('Что за зверь со мной играет? НЕ мычит, не ржёт, не лает, нападает на клубки, прячет в лапки когти.\n')
	if  a in ["Котёнок",'котёнок',"Котенок",'котенок','кот',"Кот"]:
		print("Правильно! Котёнок!\n\n\nнажми кнопку")
		msvcrt.getch()
		break
	elif i<2:
		print('\nПодумай еще!\n\nнажми кнопку')
		msvcrt.getch()
		os.system('cls')
		i=i+1
		continue
	else:
		a=input('\nНе угадал :)) \nСдаешся? ')
		if a in ['yes','y','да','д','угу']: 
			print('эхх ты... Котенок!\n\nнажми кнопку') 
			msvcrt.getch()
			os.system('cls')
			break
		else: i=0

os.system('cls')
print('СЛЕДУЮЩАЯ ЗАГАДКА\n')
i=0
while i<3:
	a=input('Маленький, желтенький, в земле ковыряется.\n')
	if  a in ["Вьетнамец",'вьетнамец',"Вьетнамец мину ищет",'Вьетнамец ищет мину',"вьетнамец мину ищет",'вьетнамец ищет мину']:
		print("Ахаха! Вьетнамец мину ищет!\n\n\nнажми кнопку")
		msvcrt.getch()
		break
	elif i<2:
		print('\nПодумай еще!\n\nнажми кнопку')
		msvcrt.getch()
		os.system('cls')
		i=i+1
		continue
	else:
		a=input('\nНе угадал :)) \nСдаешся? ')
		if a in ['yes','y','да','д','угу']: 
			print('Вьетнамец мину ищет\n\nнажми кнопку') 
			msvcrt.getch()
			os.system('cls')
			break
		else: i=0

os.system('cls')
print('СЛЕДУЮЩАЯ ЗАГАДКА\n')
i=0
while i<3:
	a=input('Маленький, желтенький в небе кувыркается.\n')
	if  a in ["Вьетнамец",'вьетнамец','Вьетнамец мину','вьетнамец мину']:
		a=input("\nПочти а дальше?\n")
		pass
	if  a in ["Вьетнамец мину нашел",'Вьетнамец ищет нашёл',"вьетнамец мину нашёл",'вьетнамец нашел мину',"нашел мину","Нашел мину","мину нашел","Мину нашел","нашёл мину","Нашёл мину","мину нашёл","Мину нашёл"]:
		a=input("\nХааа! )) Не все так просто! Но близко\n")
		pass
	if  a in ['мину нашел',"нашел мину",'Вьетнамец нашел мину']:
		print("Да! Вьетнамец мину нашел!\n\n\nнажми кнопку")
		msvcrt.getch()
		break
	elif i<2:
		print('\nНеа ))\n\nнажми кнопку')
		msvcrt.getch()
		os.system('cls')
		i=i+1
		continue
	else:
		a=input('\nНе угадал :)) \nСдаешся? ')
		if a in ['yes','y','да','д','угу']: 
			print('Вьетнамец мину нашел\n\nнажми кнопку') 
			msvcrt.getch()
			os.system('cls')
			break
		else: i=0

os.system('cls')
print('СЛЕДУЮЩАЯ ЗАГАДКА\n')
i=0
while i<3:
	a=input('В небе одна, в земле нету, а у бабы их целых две.\n')
	if  a in ["сиськи",'сиси','груди','грудь',"соски","титьки","тити","титя","сися"]:
		a=input("\nПравильно! Но ответ другой... к сожалению\n")
		pass
	if  a in ["б",'Б',"Буква Б",'Буква',"буква"]:
		print("ДА! Это буква Б!\n\n\nнажми кнопку")
		msvcrt.getch()
		break
	elif i<2:
		print('\nНеа ))\n\nнажми кнопку')
		msvcrt.getch()
		os.system('cls')
		i=i+1
		continue
	else:
		a=input('\nНе угадал :)) \nСдаешся? ')
		if a in ['yes','y','да','д','угу']: 
			print('Вьетнамец мину нашел') 
			msvcrt.getch()
			print("\nШутка.\n Ответ - Буква Б")
			msvcrt.getch()
			os.system('cls')
			break
		else: i=0

os.system('cls')
print('СЛЕДУЮЩАЯ ЗАГАДКА\n')
i=0
while i<3:
	a=input('Почему Ленин ходил в ботинках, а Сталин в сапогах?\n')
	if  len(a)>16:
		a=input("\nВау! Чувак, ответ по короче будет\n")
		pass
	if  a in ["По земле",'по земле',"земле",'земля',"на земле","Земле",'Земля',"На земле","На Земле"]:
		print("Правильно!\n\n\nнажми кнопку")
		msvcrt.getch()
		break
	elif i<2:
		print('\nНеа ))\n\nнажми кнопку')
		msvcrt.getch()
		os.system('cls')
		i=i+1
		continue
	else:
		a=input('\nНе угадал :)) \nСдаешся? ')
		if a in ['yes','y','да','д','угу']: 
			print('По земле') 
			msvcrt.getch()
			print("\nШутка.\n Ответ - Буква Б")
			msvcrt.getch()
			os.system('cls')
			break
		else: i=0

os.system('cls')
print('СЛЕДУЮЩАЯ ЗАГАДКА\n')
i=0
while i<3:
	a=input('Что это такое: синий, большой, с усами и полностью набит зайцами?\n')
	if  a in ["Троллейбус",'Тролейбус',"Тролик",'Троллик',"тралейбус","троллейбус",'тролейбус',"тролик",'троллик',"тралейбус"]:
		print("Дааа! Троллейбус\n\n\nнажми кнопку")
		msvcrt.getch()
		break
	elif i<2:
		print('\nПодумай еще!\n\nнажми кнопку')
		msvcrt.getch()
		os.system('cls')
		i=i+1
		continue
	else:
		a=input('\nНе угадал :)) \nСдаешся? ')
		if a in ['yes','y','да','д','угу']: 
			print('Это Тролейбус!') 
			msvcrt.getch()
			os.system('cls')
			break
		else: i=0

os.system('cls')
print('СЛЕДУЮЩАЯ ЗАГАДКА\n')
i=0
while i<3:
	a=input('Маленький, желтенький, дверь собою открывает.\n')
	if  a in ["Брюс",'Брюс Ли',"Брюсли",'БрюсЛи',"Ли","брюс",'брюс Ли',"брюсли",'брюсЛи',"ли",]:
		print("Брюс Ли! Киа!\n")
		msvcrt.getch()
		break
	elif i<2:
		print('\nПодумай еще!\n\nнажми кнопку')
		msvcrt.getch()
		os.system('cls')
		i=i+1
		continue
	else:
		a=input('\nНе угадал :)) \nСдаешся? ')
		if a in ['yes','y','да','д','угу']: 
			print('Это Брюс Ли!') 
			msvcrt.getch()
			os.system('cls')
			break
		else: i=0

os.system('cls')
print('СЛЕДУЮЩАЯ ЗАГАДКА\n')
i=0
while i<3:
	a=input('Что такое - маленькое, беленькое, кровь сосет?\n')
	if  a in ["Тампон",'тампон']:
		print("Хаа! Да!\n")
		msvcrt.getch()
		break
	elif i<2:
		print('\nНеа ))\n\nнажми кнопку')
		msvcrt.getch()
		os.system('cls')
		i=i+1
		continue
	else:
		a=input('\nНе угадал :)) \nСдаешся? ')
		if a in ['yes','y','да','д','угу']: 
			print('Тампон') 
			msvcrt.getch()
			os.system('cls')
			break
		else: i=0

os.system('cls')
print('СЛЕДУЮЩАЯ ЗАГАДКА\n')
i=0
while i<3:
	a=input('Без окон, без дверей, а внутри сидит еврей? Что это?\n')
	if  a in ["Сара",'сара',"беременная","Беременная","беременая","Беременая","еврейка","еврейка беременна","сара беременна","еврейка беремена","сара беремена","Еврейка","Еврейка беременна","Сара беременна","Еврейка беремена","Сара беремена"]:
		print("Да ))\n")
		msvcrt.getch()
		break
	elif i<2:
		print('\nПодумай еще\n\nнажми кнопку')
		msvcrt.getch()
		os.system('cls')
		i=i+1
		continue
	else:
		a=input('\nНе угадал :)) \nСдаешся? ')
		if a in ['yes','y','да','д','угу']: 
			print('Сара беременна') 
			msvcrt.getch()
			os.system('cls')
			break
		else: i=0

os.system('cls')
print('СЛЕДУЮЩАЯ ЗАГАДКА\n')
i=0
while i<3:
	a=input('Что такое - зеленая, нажмешь кнопку - красная?\n')
	if  a in ["миксер",'Миксер']:
		a=input("\nДа, но что внутри?\n")
		pass
	if  a in ["лягужка",'Лягужка',"Лягужка в миксере","лягужка в миксере","легужка"]:
		print("Да! Это Лягужка в миксере!\n")
		msvcrt.getch()
		break
	elif i<2:
		print('\nПодумай еще\n\nнажми кнопку')
		msvcrt.getch()
		os.system('cls')
		i=i+1
		continue
	else:
		a=input('\nНе угадал :)) \nСдаешся? ')
		if a in ['yes','y','да','д','угу']: 
			print('Лягужка в миксере )') 
			msvcrt.getch()
			os.system('cls')
			break
		else: i=0