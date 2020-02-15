# Модуль логики logic.py

expression = '' # Переменная в которую записывается ВСЁ



def press(num): 		# Подаем в функцию переменную num

	global expression 		# Загружаем глобально переменну

	expression = expression + str(num)		# конкатенация

	equation.set(expression)   	# set устанавливает значение ТКИНТЕРОВСКОЙ переменной equation = tkinter.StringVar()
								# эта переменная была объявлена в модуле GUI, но так как я отделил логику и 
								# интерфейс она перекочевала сюда. Надо что-то придумать


def equalpress():						# Нажатие РАВНО =

	try:

		global expression              # Используем переменную expression глобально

		total = str(eval(expression))   # подсчитываем значение expression, преобразуем в строку и заносим в total

		equation.set(total)           	# значение total передаем в перемененую equation

		expression = ''					# обнуляем значение expression

	except:

		equation.set(" Error ")       # Если произошла ошибка вычисления, например деление на 0, вывести на экран Error

		expression = ''				  # И обнулить expression

def clear():

	global expression

	expression = ''
	
	equation.set('')

# Модуль графического интерфейса gui.py

import tkinter 

root = tkinter.Tk()

##########################################
### Здесь вставляем начинку интерфейса ### -----------------------------------------------------------------------------------
##########################################

# Создание главного (корневого) окна калькулятора
root.geometry('300x150')         # Размеры - высота, ширина
root.configure(bg = '#f2e6d9') 	 # Цвет фона
root.title('My Calculator')		 # Заголовок главного окна

# Ткинтеровская переменная, содержимое которой выводится на экран
equation = tkinter.StringVar()

# Фрейм размещения окна дисплея
frame1 = tkinter.Frame(root, bg = '#ffb3b3') # bg - цвет заднего фона
frame1.pack()

# Окно дисплея калькулятора
display = tkinter.Entry(frame1, width = 40, textvariable = equation) # Надо посмотреть как меня высоту окна. height??
display.pack()														 # 

equation.set('Enter your expression')

# Фрейм размещения кнопок калькулятора
frame2 = tkinter.Frame(root, bg = '#9999ff')
frame2.pack()


# Кнопки калькулятора --------------------------------------------------- Кнопки калькулятора --------------------------------------
button1 = tkinter.Button(frame2 , command = lambda: press(1), text = '1', height = 1, width = 7)
button1.grid(row = 0, column = 0)
button2 = tkinter.Button(frame2 , command = lambda: press(2), text = '2', height = 1, width = 7)
button2.grid(row = 0, column = 1)
button3 = tkinter.Button(frame2 , command = lambda: press(3), text = '3', height = 1, width = 7)
button3.grid(row = 0, column = 2)
button4 = tkinter.Button(frame2 , command = lambda: press(4), text = '4', height = 1, width = 7)
button4.grid(row = 1, column = 0)
button5 = tkinter.Button(frame2 , command = lambda: press(5), text = '5', height = 1, width = 7)
button5.grid(row = 1, column = 1)
button6 = tkinter.Button(frame2 , command = lambda: press(6), text = '6', height = 1, width = 7)
button6.grid(row = 1, column = 2)
button7 = tkinter.Button(frame2 , command = lambda: press(7), text = '7', height = 1, width = 7)
button7.grid(row = 2, column = 0)
button8 = tkinter.Button(frame2 , command = lambda: press(8), text = '8', height = 1, width = 7)
button8.grid(row = 2, column = 1)
button9 = tkinter.Button(frame2 , command = lambda: press(9), text = '9', height = 1, width = 7)
button9.grid(row = 2, column = 2)
button0 = tkinter.Button(frame2 , command = lambda: press(0), text = '0', height = 1, width = 7)
button0.grid(row = 3, column = 1)
Plus = tkinter.Button(frame2 , command = lambda: press('+'), text = '+', height = 1, width = 7)
Plus.grid(row = 0, column = 3)
Minus = tkinter.Button(frame2 , command = lambda: press('-'), text = '-', height = 1, width = 7)
Minus.grid(row = 1, column = 3)
Clear = tkinter.Button(frame2 , command = clear, text = 'C', height = 1, width = 7)
Clear.grid(row = 2, column = 3)
Result = tkinter.Button(frame2, command = equalpress, text = '=', height = 1, width = 7)
Result.grid(row = 3, column = 3)
Divide = tkinter.Button(frame2 , command = lambda: press('/'), text = '/', height = 1, width = 7)
Divide.grid(row = 3, column = 0)
Mult = tkinter.Button(frame2 , command = lambda: press('*'), text = '*', height = 1, width = 7)
Mult.grid(row = 3, column = 2)
# ----------------------------------------------------------------------------------------------------------------------------------


################################
### Конец начинки интерфейса ### ----------------------------------------------------------------------------------------------------
################################

root.mainloop()
