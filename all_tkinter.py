import tkinter as tk
from tkinter import ttk


# Проверка на возможность существования такого треугольника
def is_triangle(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        return a + b + c
    else:
        return False

# Проверка, если дробное число оканчивается на .0
def zero_after_point(x):
    if x == int(x):
        return int(x)
    else:
        return x

# Настраиваем базу окна
window = tk.Tk()
window.minsize(450, 350)
window.maxsize(600, 550)
window.title("Задание 1")
frame_1 = ttk.Frame(window)
frame_1.pack(expand=True, fill="both")

# Создаём переменные, чтобы получать значения от пользователя
a_text_var = tk.StringVar()
b_text_var = tk.StringVar()
c_text_var = tk.StringVar()
result_var = tk.StringVar()


def btn_pressed():
# Пробуем конвертировать ввод в число
    try:
        # Получаем значения от пользователя и преводим их в дробные числа
        a = float(a_text_var.get())
        b = float(b_text_var.get())
        c = float(c_text_var.get())
        
        # Проводим проверку на существование треугольника. В случае существования, выводим периметр
        perimetr_float = is_triangle(a, b, c)
        
        if perimetr_float is not False:
            down_label.configure(text="Периметр треугольника равен: ")
            answ_label.place(relx=0.5, rely=0.7, anchor="center")
            perimetr_final = zero_after_point(perimetr_float)
            result_var.set(perimetr_final)
        else:
            down_label.configure(text="Такого треугольника быть не может.")
            answ_label.place_forget()

# Если пользователь ввёл не число, а строку символов выводим ошибку
    except ValueError:
        down_label.configure(text="Вместо чисел вы ввели что-то другое.")
        answ_label.place_forget()
        

# Создание класса, в котором сразу, в одной колонне будут текст и строка ввода от пользователя
class Column:
    def __init__(self, user_input, x_position, var):
        self.label = ttk.Label(frame_1, text=user_input)
        self.entry = ttk.Entry(frame_1, width=15, textvariable=var)
        self.position(x_position)

    def position(self, x_position):
        self.label.place(relx=x_position, rely=0.2, anchor="center")
        self.entry.place(relx=x_position, rely=0.3, anchor="center")


# Надпись задания сверху
label_task = ttk.Label(frame_1, text="Введите стороны А, В, С треугольника: ")
label_task.place(relx=0.5, rely=0.1, anchor="center")

# Используем заранее созданный класс, чтобы сделать три одинаковых колонки
column1 = Column(user_input="Введите число А:", x_position=0.2, var=a_text_var)
column2 = Column(user_input="Введите число B:", x_position=0.5, var=b_text_var)
column3 = Column(user_input="Введите число C:", x_position=0.8, var=c_text_var)


# Кнопка, которая передаёт введённые пользователем данные в программу и выводит результат вычислений обратно пользователю
subm_btn = ttk.Button(frame_1, text="Подсчитать", command=btn_pressed)
subm_btn.place(relx=0.5, rely=0.5, anchor="center")


# Текст, значение по-умолчанию которого изменится в том случае, если пользователь введёт вместо целых чисел что-либо другое, или если такой треугольник невозможен по правилам геометрии
down_label = ttk.Label(frame_1, text="Периметр треугольника равен: ")
down_label.place(relx=0.5, rely=0.6, anchor="center")


# Текст, который появится только в том случае, если все вычисления были проведены
answ_label = ttk.Label(frame_1, text="0", textvariable=result_var)
answ_label.place(relx=0.5, rely=0.7, anchor="center")

# Открываем окно
window.mainloop()


'''
⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨⬛⬛⬜🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨⬛⬛⬛🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬛🟨🟨🟨⬛⬛⬛🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛⬛🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬛🟨🟨🟨🟨🟧🟧⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛🟧🟧🟧🟧🟧⬛⬛🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛
⬜⬜⬛⬛⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛
⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨⬛🟨⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬛🟨⬛
⬜⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛⬛⬛🟨🟨⬛
⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛
⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜
⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜
'''


import tkinter as tk
from tkinter import ttk
from collections import Counter
from math import sqrt
import matplotlib.pyplot as plt


# Проверка на возможность существования такого треугольника
def is_triangle(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        return a + b + c
    else:
        return False


# Проверка, если дробное число оканчивается на .0
def zero_after_point(x):
    if x == int(x):
        return int(x)
    else:
        return x


# Настраиваем базу окна
window = tk.Tk()
window.minsize(500, 400)
window.title("Задание 2")
frame_1 = ttk.Frame(window)
frame_1.pack(expand=True, fill="both")


# Создаём переменные для последующего получения значений от пользователя
a_x_var = tk.StringVar()
a_y_var = tk.StringVar()
b_x_var = tk.StringVar()
b_y_var = tk.StringVar()
c_x_var = tk.StringVar()
c_y_var = tk.StringVar()
d_text_var = tk.StringVar()



def btn_pressed():
    try:
        # Создаём два пустых листа, чтобы в них положить итоговые числовые значения
        final_x = []
        final_y = []
        # Пакуем в заранее созданные листы дробные числа
        x_axis_num = [float(a_x_var.get()), float(b_x_var.get()), float(c_x_var.get())]
        y_axis_num = [float(a_y_var.get()), float(b_y_var.get()), float(c_y_var.get())]

        # Ищем дубликаты, которых больше чем 2
        x_list = Counter(x_axis_num)
        y_list = Counter(y_axis_num)
        x_axis_dupl = [item for item in x_list if x_list[item] > 2]
        y_axis_dupl = [item for item in y_list if y_list[item] > 2]

        # Проводим проверку на наличие трёх и более совпадающих координат 
        if len(x_axis_dupl) > 0 or len(y_axis_dupl) > 0:
            label_d.configure(text="Проверьте координаты, такого прямоугольника быть не может.")
            label_d_points.pack_forget()
        
        else:  
            # Если схожих координат не больше двух         
            label_d.configure(text="Координаты точки D:")
            label_d_points.pack()
            
            # Нахождение длин отрезков AB, AC, BC, выяснение что из этого гипотенуза, а что катеты
            vector_1 = sqrt(
                (x_axis_num[1] - x_axis_num[0]) ** 2
                + (y_axis_num[1] - y_axis_num[0]) ** 2
            )
            vector_2 = sqrt(
                (x_axis_num[2] - x_axis_num[0]) ** 2
                + (y_axis_num[2] - y_axis_num[0]) ** 2
            )
            vector_3 = sqrt(
                (x_axis_num[2] - x_axis_num[1]) ** 2
                + (y_axis_num[2] - y_axis_num[1]) ** 2
            )
            
            # Проверка на возможное существование такого треугольника (которая при этом избавляет от возможности что прямоугольник окажется просто отрезком)
            if is_triangle(vector_1, vector_2, vector_3):
                
                # Вычисляем что из данного - гипотенуза
                hypotenuse = max(vector_1, vector_2, vector_3)

                if hypotenuse == vector_1:
                    # Сортируем исходные листы так, чтобы координаты точки, не входящей в гипотенузу треугольника находились между координатами гипотенузы
                    sort_list = [x_axis_num[0], x_axis_num[2], x_axis_num[1]]
                    x_axis_num = sort_list
                    sort_list = [y_axis_num[0], y_axis_num[2], y_axis_num[1]]
                    
                    # Находим координаты середины гипотенузы и четвёртую точку
                    half_hypotenuse = [
                        (x_axis_num[0] + x_axis_num[2]) / 2,
                        (y_axis_num[0] + y_axis_num[2]) / 2,
                    ]
                    # Нахождение четвёртой координаты
                    d_var = [
                        (half_hypotenuse[0] * 2 - x_axis_num[1]),
                        (half_hypotenuse[1] * 2 - y_axis_num[1]),
                    ]

                elif hypotenuse == vector_2:
                    # В данном случае сортировка не нужна, лист остаётся исходным
                    half_hypotenuse = [
                        (x_axis_num[0] + x_axis_num[2]) / 2,
                        (y_axis_num[0] + y_axis_num[2]) / 2,
                    ]
                    # Нахождение четвёртой координаты
                    d_var = [
                        (half_hypotenuse[0] * 2 - x_axis_num[1]),
                        (half_hypotenuse[1] * 2 - y_axis_num[1]),
                    ]

                else:
                    # Сортируем исходные листы так, чтобы координаты точки, не входящей в гипотенузу треугольника находились между координатами гипотенузы
                    sort_list = [x_axis_num[1], x_axis_num[0], x_axis_num[2]]
                    x_axis_num = sort_list
                    sort_list = [y_axis_num[1], y_axis_num[0], y_axis_num[2]]

                    # Находим координаты середины гипотенузы и четвёртую точку
                    half_hypotenuse = [
                        (x_axis_num[0] + x_axis_num[2]) / 2,
                        (y_axis_num[0] + y_axis_num[2]) / 2,
                    ]
                    # Нахождение четвёртой координаты
                    d_var = [
                        (half_hypotenuse[0] * 2 - x_axis_num[1]),
                        (half_hypotenuse[1] * 2 - y_axis_num[1]),
                    ]

                # Добавляем четвёртую точку в листы х и у, и ещё раз первую, чтобы начертить прямоугольник
                x_axis_num.append(d_var[0])
                y_axis_num.append(d_var[1])
                x_axis_num.append(x_axis_num[0])
                y_axis_num.append(y_axis_num[0])

                # Обрубаем все лишние .0, если такие есть и вносим значения в итоговый лист
                for i in x_axis_num:
                    final_x.append(zero_after_point(i))
                for j in y_axis_num:
                    final_y.append(zero_after_point(j))

                
                # Чтобы было удобнее вывести четвёртую координату (буквы выбраны случайно, могут не совпадать с реальностью)
                # A = [final_x[0], final_y[0]]
                # B = [final_x[1], final_y[1]]
                # C = [final_x[2], final_y[2]]
                D = [final_x[3], final_y[3]]
                d_text_var.set(f'{D[0]}.{D[1]}')            
            

                # Закрываем открытые до этого графики
                plt.close(fig="all")
                # Создаём фигуру
                plt.figure(num="rectangle", dpi=100)

                # Настраиваем график
                plt.grid(visible=True, linewidth=1, which="both")
                plt.title(label="Прямоугольник", fontsize=14)

                plt.xlabel(xlabel="Ось X", loc="center")
                plt.ylabel(ylabel="Ось Y", loc="center")

                # Выводим
                plt.plot(final_x, final_y)
                plt.show()

            else:
                # В случае, если проверка на существование треугольника не пройдена
                label_d.configure(text="Проверьте координаты, такого прямоугольника быть не может.")
                label_d_points.pack_forget()
        

    except ValueError:
        # Если пользователь ввёл что-то вместо чисел
        label_d.configure(text="Вместо чисел вы ввели что-то другое.")
        label_d_points.pack_forget()



# Создание класса, в котором сразу, в одной строке будут текст и две строки ввода от пользователя
class Row:
    def __init__(self, user_input, y_position, var_x, var_y):
        self.label = ttk.Label(frame_1, text=user_input)
        self.entry_x = ttk.Entry(frame_1, textvariable=var_x)
        self.entry_y = ttk.Entry(frame_1, textvariable=var_y)
        self.position(y_position)

    def position(self, y_position):
        self.label.place(relx=0.3, rely=y_position, anchor="center")
        self.entry_x.place(relx=0.4, rely=y_position, anchor="center", relwidth=0.1)
        self.entry_y.place(relx=0.5, rely=y_position, anchor="w", relwidth=0.1)


# Надпись задания сверху
label_task = ttk.Label(
    frame_1, text="Введите координаты точек А, В, С прямоугольника: "
)
label_task.place(relx=0.5, rely=0.1, anchor="center")


# Надписи х и у над соответствующими колонками
label_x = ttk.Label(frame_1, text="x")
label_y = ttk.Label(frame_1, text="y")
label_x.place(relx=0.4, rely=0.2, anchor="w", relwidth=0.1)
label_y.place(relx=0.6, rely=0.2, anchor="center", relwidth=0.1)


# Строки с вводом координат А, В, С
row_a = Row(user_input="A", y_position=0.3, var_x=a_x_var, var_y=a_y_var)
row_b = Row(user_input="B", y_position=0.4, var_x=b_x_var, var_y=b_y_var)
row_c = Row(user_input="C", y_position=0.5, var_x=c_x_var, var_y=c_y_var)

# Кнопка приёма данных пользователя
btn = ttk.Button(frame_1, text="Построить", command=btn_pressed)
btn.place(relx=0.7, rely=0.5, anchor="center")

# Создаём frame, строку, которая будет выводить координаты точки D прямоугольника
frame_2 = ttk.Frame(frame_1, width=50, height=50)
label_d = ttk.Label(frame_2, text="Координаты точки D:")
label_d_points = ttk.Label(frame_2, text="0.0", textvariable=d_text_var)

frame_2.place(relx=0.5, rely=0.6, anchor="center")
label_d.pack(side="left", padx=(0, 5))
label_d_points.pack()

# Открываем окно
window.mainloop()


'''
⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨⬛⬛⬜🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨⬛⬛⬛🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬛🟨🟨🟨⬛⬛⬛🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛⬛🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬛🟨🟨🟨🟨🟧🟧⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛🟧🟧🟧🟧🟧⬛⬛🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛
⬜⬜⬛⬛⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛
⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨⬛🟨⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬛🟨⬛
⬜⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛⬛⬛🟨🟨⬛
⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛
⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜
⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜
'''


import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt


# Проверка, если дробное число оканчивается на .0
def zero_after_point(x):
    if x == int(x):
        return int(x)
    else:
        return x


# Настраиваем базу окна
window = tk.Tk()
window.minsize(450, 350)
window.maxsize(600, 550)
window.title("Задание 3")
frame_1 = ttk.Frame(window)
frame_1.pack(expand=True, fill="both")


# Создаём переменные, чтобы получать значения от пользователя
point_x_str = tk.StringVar()
point_y_str = tk.StringVar()
quadrant_str = tk.StringVar()


def btn_pressed():

    try:
        label_down.configure(text="Находится:")
        label_quadrant.pack()
        # Получаем координаты точки
        point_x = float(point_x_str.get())
        point_y = float(point_y_str.get())

        x = zero_after_point(point_x)
        y = zero_after_point(point_y)

        # Определение, в какой четверти находится точка ()
        if x > 0 and y > 0:
            dot = "в 1 четверти"
        elif x > 0 and y < 0:
            dot = "в 4 четверти"
        elif (x > 0 and y == 0) or (x < 0 and y == 0):
            dot = "на оси X"
        elif x == 0 and y == 0:
            dot = "в начале координат"
        elif (x == 0 and y < 0) or (x == 0 and y > 0):
            dot = "на оси Y"
        elif x < 0 and y > 0:
            dot = "во 2 четверти"
        else:
            dot = "в 3 четверти"

        quadrant_str.set(dot)

        # Закрываем открытые до этого графики
        plt.close(fig="all")
        # Создаём фигуру
        plt.figure(num="dot", dpi=100)

        # Настраиваем график
        plt.title(label="Точка", fontsize=14)
        plt.xlabel(xlabel="Ось X", loc="center")
        plt.ylabel(ylabel="Ось Y", loc="center")

        # Выводим
        plt.plot(x, y, "ro")
        plt.show()

    except ValueError:
        # Если пользователь ввёл что-то вместо чисел
        label_down.configure(text="Вместо чисел вы ввели что-то другое.")
        label_quadrant.pack_forget()


# Создаём колонку с названием, строокой ввода
class Column:
    def __init__(self, parent, column_text, var, x, y):
        self.frame = ttk.Frame(parent)
        self.label = ttk.Label(self.frame, text=column_text)
        self.entry = ttk.Entry(self.frame, textvariable=var, width=8)
        self.position(x, y)
        
    def position(self, x, y):
        self.frame.place(relx=x, rely=y, anchor="center")
        self.label.pack()
        self.entry.pack()

# Надпись задания сверху
label_task = ttk.Label(frame_1, text="Введите координаты точки:")
label_task.place(relx=0.5, rely=0.1, anchor="center")

# Колонка 1
column_1 = Column(frame_1, column_text="X", var=point_x_str, x=0.4, y=0.3)

# Колонка 2
column_2 = Column(frame_1, column_text="Y", var=point_y_str, x=0.6, y=0.3)



# Кнопка приёма данных пользователя
btn = ttk.Button(frame_1, text="Показать графически", command=btn_pressed)
btn.place(relx=0.5, rely=0.5, anchor="center")

# Создаём frame, строку, которая будет выводить в какой четверти находится точка
frame_2 = ttk.Frame(frame_1, width=50, height=50)
label_down = ttk.Label(frame_2, text="Находится:")
label_quadrant = ttk.Label(frame_2, text="0", textvariable=quadrant_str)

frame_2.place(relx=0.5, rely=0.6, anchor="center")
label_down.pack()
label_quadrant.pack()

# Открываем окно
window.mainloop()

'''
⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨⬛⬛⬜🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨⬛⬛⬛🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬛🟨🟨🟨⬛⬛⬛🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛⬛🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬛🟨🟨🟨🟨🟧🟧⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛🟧🟧🟧🟧🟧⬛⬛🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛
⬜⬜⬛⬛⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛
⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨⬛🟨⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬛🟨⬛
⬜⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛⬛⬛🟨🟨⬛
⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛
⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜
⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜
'''

import tkinter as tk
from tkinter import ttk


# Настраиваем базу окна
window = tk.Tk()
window.minsize(500, 400)
window.title("Задание 4")
frame_1 = ttk.Frame(window)
frame_1.pack(expand=True, fill="both")


user_inp = tk.StringVar()

def btn_pressed():
    # Получаем ввод пользователя
    str_var = user_inp.get()
    # Готовим новую строку
    new_str = ""
    for i in str_var:
        # Меняем регистры
        if i.isupper():
            new_str += i.lower()
        else:
            new_str += i.upper()
    # Выводим новую строку
    new_str_label.configure(text=new_str)




# Надпись задания сверху
label_task = ttk.Label(frame_1, text="Перевести символы нижнего регистра в верхний и наоборот")
label_task.place(relx=0.5, rely=0.1, anchor="center")

# Отдел с label и строкой для пользовательского ввода
frame_a = ttk.Frame(frame_1)
frame_a.place(relx=0.5, rely=0.2, anchor="center")
a_label = ttk.Label(frame_a, text="Введите строку:")
a_inp = ttk.Entry(frame_a, textvariable=user_inp)
a_label.pack()
a_inp.pack()

# Отдел с кнопкой и конечным выводом
frame_b = ttk.Frame(frame_1)
frame_b.place(relx=0.5, rely=0.4, anchor="center")
btn = ttk.Button(frame_b, text="Конвертировать", command=btn_pressed)
new_str_label = ttk.Label(frame_b, text="Здесь будет новая строка")
btn.pack()
new_str_label.pack()


# Открываем окно
window.mainloop()

'''
⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨⬛⬛⬜🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨⬛⬛⬛🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬛🟨🟨🟨⬛⬛⬛🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛⬛🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬛🟨🟨🟨🟨🟧🟧⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛🟧🟧🟧🟧🟧⬛⬛🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛
⬜⬜⬛⬛⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛
⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨⬛🟨⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬛🟨⬛
⬜⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛⬛⬛🟨🟨⬛
⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛
⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜
⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜
'''

import tkinter as tk
from tkinter import ttk
import random as r
import string as s


# Настраиваем базу окна
window = tk.Tk()
window.minsize(500, 400)
window.title("Задание 5")
frame_1 = ttk.Frame(window)
frame_1.pack(expand=True, fill="both")


# Готовый лист с русскими буквами
rus_list = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я","А","Б","В","г","Д","Е","Ё","Ж","З","И","Й","К","Л","М","Н","О","П","Р","С","Т","У","Ф","Х","Ц","Ч","Ш","Щ","Ъ","Ы","Ь","Э","Ю","Я"]


def random_power(choice):
    if choice == 1:
        # Выбираем случайную букву нижнего регистра из английского алфавита
        char = r.choice(s.ascii_lowercase)
        return char
    elif choice == 2:
        # Выбираем случайную букву верхнего регистра из английского алфавита
        char = r.choice(s.ascii_uppercase)
        return char
    elif choice == 3:
        # Выбираем случайную букву любого регистра из русского алфавита
        char = r.choice(rus_list)
        return char
    elif choice == 4:
        # Выбираем случайную цифру от 1 до 10 (выбрано для удобства отображения в маленьком окне)
        char = r.randint(1,10)
        return char
    else:
        # Выбираем любые другие знаки, не вошедшие в предыдущие категории
        char = r.choice(s.punctuation)
        return char


def create_array():
    # Создаём пустой лист с вложенными листами
    array = [
        [],
        [],
        [],
        [],
        [],
    ]

    # Наполняем лист случайными символами/числами/буквами
    for row in array:
        for item in range(5):
            # Выбираем категорию, из которой будет символ
            random_choice = r.randint(1, 5)
            # Добавляем его во вложенный лист
            row.append(random_power(random_choice))
    
    # Показываем листы пользователю        
    label_array.configure(text=f"{array[0]}\n{array[1]}\n{array[2]}\n{array[3]}\n{array[4]}")

    return change_array(array)


def change_array(array):
    # Создаём счётчики для удобства обнуления диагоналей
    main_diagonal = 0
    sub_diagonal = 4

    # Обнуляем значения, у которых индекс такой же, как у счётчиков, изменяем счётчики
    for outer in range(5):
        array[outer][main_diagonal] = 0
        array[outer][sub_diagonal] = 0
        main_diagonal += 1
        sub_diagonal -= 1

    # Показываем изменённые листы пользователю
    label_new_array.configure(text=f"{array[0]}\n{array[1]}\n{array[2]}\n{array[3]}\n{array[4]}")


# Надпись задания сверху
label_task = ttk.Label(frame_1, text="Обнулить в массиве главную и побочную диагонали.")
label_task.place(relx=0.5, rely=0.1, anchor="center")

# Исходный массив
label_array = ttk.Label(frame_1, text='', wraplength=350, font="12")
label_array.place(relx=0.3, rely=0.3, anchor="center")

# Новый массив с обнулёнными диагоналями
label_new_array = ttk.Label(frame_1, text='', wraplength=350, font="12")
label_new_array.place(relx=0.7, rely=0.3, anchor="center")

# Кнопка действия
btn_create = ttk.Button(frame_1, text="Создать массив и обнулить диагонали", command=create_array)
btn_create.place(relx=0.5, rely=0.6, anchor="center")


# Открываем окно
window.mainloop()

'''
⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨⬛⬛⬜🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨⬛⬛⬛🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬛🟨🟨🟨⬛⬛⬛🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛⬛🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬛🟨🟨🟨🟨🟧🟧⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛🟧🟧🟧🟧🟧⬛⬛🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛
⬜⬜⬛⬛⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛
⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨⬛🟨⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬛🟨⬛
⬜⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛⬛⬛🟨🟨⬛
⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛
⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜
⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜
'''

import tkinter as tk
from tkinter import ttk


# Настраиваем базу окна
window = tk.Tk()
window.minsize(500, 400)
window.title("Задание 6")
frame_1 = ttk.Frame(window)
frame_1.pack(expand=True, fill="both")

# Переменная для принятия ввода от пользователя
user_inp = tk.StringVar()

# Заранее заготовленный список гласных в русском и английском языках
vowels = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я", "a", "e", "i", "o", "u"]

# Выполняется после нажатия кнопки
def btn_pressed():
    # Получаем значение из строки ввода
    str_var = user_inp.get()
    # Приводим всё к единому формату (все буквы маленькие)
    str_var = str_var.lower()
    # Создаём счётчик букв и считаем только те, что есть в нашем готовом листе
    vowels_cnt = 0
    for i in str_var:
        if i in vowels:
            vowels_cnt += 1
    
    # Меняем текст на получившееся количество букв
    cnt_vowels.configure(text=f"{vowels_cnt}")
    
        
# Надпись задания сверху
label_task = ttk.Label(frame_1, text="Определить количество глассных букв")
label_task.place(relx=0.5, rely=0.1, anchor="center")

# Создаём отдельно строку и ввод, для удобства пакуем в frame_a
frame_a = ttk.Frame(frame_1)
frame_a.place(relx=0.5, rely=0.2, anchor="center")
a_label = ttk.Label(frame_a, text="Введите строку:")
a_inp = ttk.Entry(frame_a, textvariable=user_inp)
a_label.pack()
a_inp.pack()

# Создаём отдельно кнопку, и две строки, для удобства пакуем в frame_b
frame_b = ttk.Frame(frame_1)
frame_b.place(relx=0.5, rely=0.4, anchor="center")
btn = ttk.Button(frame_b, text="Определить количество гласных", command=btn_pressed)
new_str_label = ttk.Label(frame_b, text="Количество гласных в предложении:")
# Будет показывать количество гласных
cnt_vowels = ttk.Label(frame_b, text="")
btn.pack()
new_str_label.pack()
cnt_vowels.pack()

# Открываем окно
window.mainloop()

'''
⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨⬛⬛⬜🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨⬛⬛⬛🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬛🟨🟨🟨⬛⬛⬛🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛⬛🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬛🟨🟨🟨🟨🟧🟧⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛🟧🟧🟧🟧🟧⬛⬛🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛
⬜⬜⬛⬛⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛
⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨⬛🟨⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬛🟨⬛
⬜⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛⬛⬛🟨🟨⬛
⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛
⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜
⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜
'''

import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt



# Настраиваем базу окна
window = tk.Tk()
window.minsize(500, 400)
window.title("Задание 7")
frame_1 = ttk.Frame(window)
frame_1.pack(expand=True, fill="both")



def btn_pressed():
    
    # Записали неравенства
    def eq_1(x):
        return x**2 - 2*x + 3
    
    def eq_2(x):
        return -x + 7
        
    # Устанавливаем диапазон (вручную подобранный)
    x_min, x_max = -5, 5
    y_min, y_max = -10, 10
    
    # Создаём массивы х и у, в промежутке которых будем работать
    x_points = np.arange(x_min, x_max + 1)
    y_points = np.arange(y_min, y_max + 1)
    
    # Вычисление общих целых точек
    int_points = []
    for x in x_points:
        for y in y_points:
            if y > eq_1(x) and y < eq_2(x):
                int_points.append((x, y))
    
    # Делаем из листа массив
    int_points = np.array(int_points)
    
    
    # Считаем сколько точек получилось 
    cnt = len(int_points)
    row_3.inequation.configure(text=f"{cnt}")
    
    # Настраиваем график
    plt.figure(num="my_figure", dpi=100)
    plt.grid(visible=True, linewidth=1)

    # Строим основные графики
    x = np.linspace(x_min, x_max)
    y1 = eq_1(x)
    y2 = eq_2(x)
    plt.plot(x, y1)
    plt.plot(x, y2)
    
    # Ставим точки на целых числах
    if int_points.size > 0:
        plt.scatter(int_points[:, 0], int_points[:, 1], color='red', label='Целые точки')

    # Показываем фигуру
    plt.show()
    
    


# Класс, состоящий из двух label. Одна говорит какое по счёту это неравенство, вторая отображает само неравенство
class Row:
    def __init__(self, parent, user_input, inequation):
        self.label = ttk.Label(parent, text=user_input)
        self.inequation = ttk.Label(parent, text=inequation)
        self.label.pack(side="left", padx=(0, 5))
        self.inequation.pack()


# Надпись задания сверху
label_task = ttk.Label(frame_1, text="№ 70:")
label_task.place(relx=0.5, rely=0.1, anchor="center")

# Первое неравенство
frame_a = ttk.Frame(frame_1)
frame_a.place(relx=0.5, rely=0.2, anchor="center")
row_1 = Row(parent=frame_a, user_input="Первое:", inequation="y > x^2 - 2*x + 3")

# Второе неравенство
frame_b = ttk.Frame(frame_1)
frame_b.place(relx=0.5, rely=0.3, anchor="center")
row_2 = Row(parent=frame_b, user_input="Второе:", inequation="y < -x + 7")

# Кнопка действия
btn = ttk.Button(frame_1, text="Показать графически", command=btn_pressed)
btn.place(relx=0.5, rely=0.4, anchor="center")

# Label с количеством целых точек
frame_cnt = ttk.Frame(frame_1)
frame_cnt.place(relx=0.5, rely=0.5, anchor="center")
row_3 = Row(parent=frame_cnt, user_input="Всего точек:", inequation=0)


# Открываем окно
window.mainloop()

'''
⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨⬛⬛⬜🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨⬛⬛⬛🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬛🟨🟨🟨⬛⬛⬛🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛⬛🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬛🟨🟨🟨🟨🟧🟧⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛🟧🟧🟧🟧🟧⬛⬛🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛
⬜⬜⬛⬛⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛
⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨⬛🟨⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬛🟨⬛
⬜⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛⬛⬛🟨🟨⬛
⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛
⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜
⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜
'''

import tkinter as tk
from tkinter import ttk
import re

# Настраиваем базу окна
window = tk.Tk()
window.minsize(500, 400)
window.title("Задание 8")
tabs = ttk.Notebook(window)
tabs.pack(expand=True, fill="both")


class Excercise:
    def __init__(self, name, task_text, btn_command):
        self.frame = ttk.Frame(tabs)
        self.frame.pack(expand=True, fill="both")
        tabs.add(self.frame, text=name)

        # Создаём label с заданием
        self.task_label = ttk.Label(self.frame, text=task_text, wraplength=350)

        # Создаём поле для ввода текста
        self.text_input = tk.Text(self.frame)

        # Кнопка для приёма данных от пользователя
        self.btn = ttk.Button(self.frame, text="Вывести результат", command=btn_command)

        # label для вывода итогового текста
        self.output_label = ttk.Label(self.frame, text="", wraplength=350, font="12")

        self.position()

    # Расставляем всё по местам
    def position(self):

        self.task_label.place(relx=0.5, rely=0.1, anchor="center")
        self.text_input.place(
            relx=0.5, rely=0.4, relheight=0.3, relwidth=0.5, anchor="center"
        )
        self.btn.place(relx=0.5, rely=0.6, anchor="center")
        self.output_label.place(relx=0.5, rely=0.8, anchor="center")



# Задание 8_1
def punctuation():
    inp = exercise_8_1.text_input.get(1.0, "end-1c")
    # Не оставляет пробел вместо знаков "_", но я и не думаю, что это возможно, да и нужно
    new_str = re.sub(r'[^\w\s]|_', '', inp)
    exercise_8_1.output_label.configure(text=new_str)

exercise_8_1 = Excercise(
    name="8_1",
    task_text='С помощью регулярных выражений уберите все символы пунктуации из предложения',
    btn_command=punctuation,
)


# Задание 8_2
def tandem():
    inp = exercise_8_2.text_input.get(1.0, "end-1c")
    pattern = r'\b(\w+)\1\b'
    def has_tandem_repetition(line): 
        return bool(pattern.search(line))
    new_str = [line for line in inp.split('\n') if has_tandem_repetition(line)]
    exercise_8_2.output_label.configure(text=new_str)

exercise_8_2 = Excercise(
    name="8_2",
    task_text='Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).',
    btn_command=tandem,
)

# Задание 8_3
def print_cat_cat():
    inp = exercise_8_3.text_input.get(1.0, "end-1c")
    new_str = "\n".join(re.findall(r'(cat.*cat)', inp, re.MULTILINE)) 
    exercise_8_3.output_label.configure(text=new_str)

exercise_8_3 = Excercise(
    name="8_3",
    task_text='Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.',
    btn_command=print_cat_cat,
)


# Задание 8_4
def print_cat():
    inp = exercise_8_4.text_input.get(1.0, "end-1c")
    new_str = "\n".join(re.findall(r'(^.*\bcat\b.*$)', inp, re.MULTILINE)) 
    exercise_8_4.output_label.configure(text=new_str)

exercise_8_4 = Excercise(
    name="8_4",
    task_text='Выведите строки, содержащие "cat" в качестве слова.',
    btn_command=print_cat,
)

# Задание 8_5
def print_backslash():
    inp = exercise_8_5.text_input.get(1.0, "end-1c")
    new_str = "\n".join(re.findall(r'.*\\.*', inp, re.MULTILINE)) 
    exercise_8_5.output_label.configure(text=new_str)


exercise_8_5 = Excercise(
    name="8_5",
    task_text='Выведите строки, содержащие обратный слеш "\\".',
    btn_command=print_backslash,
)

# Задание 8_6
def change_to_computer():
    inp = exercise_8_6.text_input.get(1.0, "end-1c")
    new_str = re.sub(r'human', 'computer', inp)
    exercise_8_6.output_label.configure(text=new_str)

exercise_8_6 = Excercise(
    name="8_6",
    task_text="В каждой строке замените все вхождения подстроки \"human\" на подстроку \"computer\" и выведите полученные строки.",
    btn_command=change_to_computer,
)


# Задание 8_7
def change_to_argh():
    inp = exercise_8_7.text_input.get(1.0, "end-1c")
    new_str = re.sub(r'\b[aA]+\b', 'argh', inp, count=1)
    exercise_8_7.output_label.configure(text=new_str)

exercise_8_7 = Excercise(
    name="8_7",
    task_text="В каждой строке замените первое вхождение слова, состоящего только из латинских букв \"a\" (регистр не важен), на слово \"argh\".",
    btn_command=change_to_argh,
)

# Задание 8_8
def swap_two_first_letters():
    inp = exercise_8_8.text_input.get(1.0, "end-1c")
    
    def swap(found):
        word = found.group()
        return word[1] + word[0] + word[2:]
    
    new_str = re.sub(r"\w[a-zA-Z0-9а-яА-Я]{1,}", swap, inp)
    exercise_8_8.output_label.configure(text=new_str)

exercise_8_8 = Excercise(
    name="8_8",
    task_text="В каждой строке поменяйте местами две первые буквы каждого слова, состоящего хотя бы из двух букв.",
    btn_command=swap_two_first_letters,
)

# Задание 8_9
def several_letters_to_one():
    inp = exercise_8_9.text_input.get(1.0, "end-1c")
    new_str = re.sub(r"([a-zA-Z0-9а-яА-Я])\1{1,}", r"\1", inp)
    exercise_8_9.output_label.configure(text=new_str)

exercise_8_9 = Excercise(
    name="8_9",
    task_text="В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.",
    btn_command=several_letters_to_one,
)

# Задание 8_10
def email_work():
    inp = exercise_8_10.text_input.get(1.0, "end-1c")
    pattern = r'(\w+)@(\w+)\.(\w+)'
    new_str = re.findall(pattern, inp)
    exercise_8_10.output_label.configure(text=new_str)

exercise_8_10 = Excercise(
    name="8_10",
    task_text="Извлеките никнейм пользователя, имя домена и суффикс из данных email адресов",
    btn_command=email_work,
)

# Открываем окно
window.mainloop()


'''
⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨⬛⬛⬜🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨⬛⬛⬛🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬛🟨🟨🟨⬛⬛⬛🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛⬛🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬛🟨🟨🟨🟨🟧🟧⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛🟧🟧🟧🟧🟧⬛⬛🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛
⬜⬜⬛⬛⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛
⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨⬛🟨⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬛🟨⬛
⬜⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛⬛⬛🟨🟨⬛
⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛
⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜
⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜
⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜
'''

import tkinter as tk
from tkinter import ttk
import re

# Настраиваем базу окна
window = tk.Tk()
window.minsize(500, 400)
window.title("Задание 9")
frame_1 = ttk.Frame(window)
frame_1.pack(expand=True, fill="both")


# Создаём паттерны по которым будем вычислять в тексте нужные элементы
name_pattern = r'[А-ЯЁ][а-яё]+\s[А-ЯЁ]\.[А-ЯЁ]\.'
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
phone_pattern = r'\+7\(\d{3}\)\d{3}-\d{2}-\d{2}'

def btn_pressed():
    # Получаем ввод пользователя
    text = str_var.get()
    # Ищем по паттернам нужные элементы
    fio = re.search(name_pattern, text).group()
    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)
    # Меняем текст, выводим результат
    result_label.configure(text=f'ФИО: {fio} \nEmail: {emails} \nТелефон: {phones} ')


# Переменная для принятия ввода от пользователя
str_var = tk.StringVar()
# Надпись задания сверху
task_label = ttk.Label(frame_1, text="Введите строку из которой нужно извлечь ФИО, телефон и email:")
task_label.place(relx=0.5, rely=0.1, anchor="center")

# Строка пользовательского ввода
enter = ttk.Entry(frame_1, textvariable=str_var)
enter.place(relx=0.5, rely=0.3, anchor="center")

# Кнопка, запускающая механизм извлечения
btn = ttk.Button(frame_1, text="Извлечь", command=btn_pressed)
btn.place(relx=0.5, rely=0.4, anchor="center")

# Label, куда будем выводить наш результат
result_label = ttk.Label(frame_1, text="ФИО: - \nEmail: - \nТелефон: - ")
result_label.place(relx=0.5, rely=0.5, anchor="center")



# Открываем окно
window.mainloop()


'''студент Петров В.П. - группа УМР11 тел. +7(918)240-04-40
Email: petrov@mail.ru доп. тел +7(926)718-33-22'''