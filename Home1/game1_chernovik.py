import os
import msvcrt
os.system('cls')
print('СЛЕДУЮЩАЯ ЗАГАДКА\n')
i=0
while i<3:
	a=input('Маленький, желтенький в небе кувыркается.\n')
	if  a in ["Вьетнамец",'вьетнамец','Вьетнамец мину','вьетнамец мину']:
		input("\nПочти а дальше?\n")
		pass
	if  a in ["Вьетнамец мину ищет",'Вьетнамец ищет мину',"вьетнамец мину ищет",'вьетнамец ищет мину']:
		input("\nХааа! )) Не все так просто! Но близко\n")
		pass
	if  a in ['мину нашел',"нашел мину",'Вьетнамец нашел мину']:
		print("Да! Вьетнамец мину нашел!\n")
		msvcrt.getch()
		break
	elif i<2:
		print('\nНеа ))')
		msvcrt.getch()
		os.system('cls')
		i=i+1
		continue
	else:
		a=input('\nНе угадал :)) \nСдаешся? ')
		if a in ['yes','y','да','д','угу']: 
			print('Вьетнамец мину нашел') 
			msvcrt.getch()
			os.system('cls')
			break
		else: i=0