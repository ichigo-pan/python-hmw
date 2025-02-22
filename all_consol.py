a, b, c = map(int, input('Введите стороны А, В, С треугольника: ').split())
# Проверяем существует ли такой треугольник, если да - считаем периметр
if (a + b > c) and (a + c > b) and (b + c > a):
    perimetr = a + b + c
    print(f'Периметр треугольника равен: {perimetr}')
else:
    print("Такой треугольник не может существовать.")
    
'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⡿⠻⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣿⠁⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⡇⠀⠀⠀⠀⠹⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⣿⡇⠀⠀⠀⠀⠀⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡟⣿⣦⣀⠀⣀⣼⠁⣿⣿⠀⠲⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡇⠈⢛⣿⠿⢿⣿⡄⠘⢻⡇⠀⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⡇⣴⠋⠀⠀⣀⠈⠙⣄⠈⡇⠀⢰⠀⣀⠤⠐⠶⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠹⣇⢰⣷⣾⠷⢶⣤⡘⣤⠇⠀⠞⠋⠀⠀⣀⣠⣤⣴⣶⣶⣶⣶⣦⣤⣀⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⣿⣧⣄⡀⠙⣿⣿⣠⡟⢀⡤⠒⠉⠉⠉⠉⠛⣫⠟⠋⠉⠉⠉⠛⠻⢿⣶⣄
⠀⠀⠀⢀⣤⣶⣾⣿⣿⠶⠿⠿⢦⣙⣦⣿⣿⣿⣾⣟⣉⡉⠉⠙⠶⣶⣿⡇⠀⠀⠀⠀⠀⠀⢀⣴⡿⠁
⠀⢀⣴⣿⣿⣿⣟⣁⣀⣀⣤⠔⢒⣿⣿⣿⣿⠿⣍⡀⠉⠻⣶⡆⠀⠘⣿⣷⣄⠀⠀⠀⣀⣴⠿⠋⠀⠀
⢠⡾⠋⠁⠀⢹⣿⡿⠋⣡⣏⠤⠋⣱⡿⢻⡟⡓⢦⣽⣦⣴⣿⣧⠂⢠⡏⠙⠻⢿⣿⣿⠟⠁⠀⠀⠀⠀
⣿⣧⣤⣤⣤⣾⡯⠤⠚⠋⠁⠀⢰⠟⠀⡞⢀⡇⠈⢿⡟⠯⣭⣤⣴⣋⣠⡤⠶⠛⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⣧⠊⣧⠀⢸⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⣰⣿⣧⣸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⡿⠟⠻⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⢸⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣄⣠⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''

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

point_1, point_2, point_3 = input("Введите координаты трёх точек прямоугольника в формате x1,y1 x2,y2 x3,y3: ").split()

# Отделяем координаты x от y
x1, y1 = map(int, point_1.split(","))
x2, y2 = map(int, point_2.split(","))
x3, y3 = map(int, point_3.split(","))
# Создаём два пустых листа, чтобы в них положить итоговые числовые значения
final_x = []
final_y = []
# Пакуем в заранее созданные листы дробные числа
x_axis_num = [x1, x2, x3]
y_axis_num = [y1, y2, y3]

# Ищем дубликаты, которых больше чем 2
x_list = Counter(x_axis_num)
y_list = Counter(y_axis_num)
x_axis_dupl = [item for item in x_list if x_list[item] > 2]
y_axis_dupl = [item for item in y_list if y_list[item] > 2]

# Проводим проверку на наличие трёх и более совпадающих координат 
if len(x_axis_dupl) > 0 or len(y_axis_dupl) > 0:
    print("Перепроверьте координаты, такого прямоугольника быть не может")

else:  
    # Если схожих координат не больше двух         
    
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
        print(f'Координаты четвёртой точки: {D}')
        
        
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
        print("Проверьте координаты, такого прямоугольника быть не может.")

'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⡿⠻⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣿⠁⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⡇⠀⠀⠀⠀⠹⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⣿⡇⠀⠀⠀⠀⠀⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡟⣿⣦⣀⠀⣀⣼⠁⣿⣿⠀⠲⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡇⠈⢛⣿⠿⢿⣿⡄⠘⢻⡇⠀⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⡇⣴⠋⠀⠀⣀⠈⠙⣄⠈⡇⠀⢰⠀⣀⠤⠐⠶⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠹⣇⢰⣷⣾⠷⢶⣤⡘⣤⠇⠀⠞⠋⠀⠀⣀⣠⣤⣴⣶⣶⣶⣶⣦⣤⣀⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⣿⣧⣄⡀⠙⣿⣿⣠⡟⢀⡤⠒⠉⠉⠉⠉⠛⣫⠟⠋⠉⠉⠉⠛⠻⢿⣶⣄
⠀⠀⠀⢀⣤⣶⣾⣿⣿⠶⠿⠿⢦⣙⣦⣿⣿⣿⣾⣟⣉⡉⠉⠙⠶⣶⣿⡇⠀⠀⠀⠀⠀⠀⢀⣴⡿⠁
⠀⢀⣴⣿⣿⣿⣟⣁⣀⣀⣤⠔⢒⣿⣿⣿⣿⠿⣍⡀⠉⠻⣶⡆⠀⠘⣿⣷⣄⠀⠀⠀⣀⣴⠿⠋⠀⠀
⢠⡾⠋⠁⠀⢹⣿⡿⠋⣡⣏⠤⠋⣱⡿⢻⡟⡓⢦⣽⣦⣴⣿⣧⠂⢠⡏⠙⠻⢿⣿⣿⠟⠁⠀⠀⠀⠀
⣿⣧⣤⣤⣤⣾⡯⠤⠚⠋⠁⠀⢰⠟⠀⡞⢀⡇⠈⢿⡟⠯⣭⣤⣴⣋⣠⡤⠶⠛⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⣧⠊⣧⠀⢸⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⣰⣿⣧⣸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⡿⠟⠻⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⢸⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣄⣠⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''

import matplotlib.pyplot as plt


# Проверка, если дробное число оканчивается на .0
def zero_after_point(x):
    if x == int(x):
        return int(x)
    else:
        return x
    
    
# Получаем координаты точки
point_x, point_y = map(float, input('Введите координаты точки в формате x,y: ').split(','))

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

print(f'Точка находится {dot}')

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


'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⡿⠻⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣿⠁⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⡇⠀⠀⠀⠀⠹⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⣿⡇⠀⠀⠀⠀⠀⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡟⣿⣦⣀⠀⣀⣼⠁⣿⣿⠀⠲⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡇⠈⢛⣿⠿⢿⣿⡄⠘⢻⡇⠀⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⡇⣴⠋⠀⠀⣀⠈⠙⣄⠈⡇⠀⢰⠀⣀⠤⠐⠶⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠹⣇⢰⣷⣾⠷⢶⣤⡘⣤⠇⠀⠞⠋⠀⠀⣀⣠⣤⣴⣶⣶⣶⣶⣦⣤⣀⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⣿⣧⣄⡀⠙⣿⣿⣠⡟⢀⡤⠒⠉⠉⠉⠉⠛⣫⠟⠋⠉⠉⠉⠛⠻⢿⣶⣄
⠀⠀⠀⢀⣤⣶⣾⣿⣿⠶⠿⠿⢦⣙⣦⣿⣿⣿⣾⣟⣉⡉⠉⠙⠶⣶⣿⡇⠀⠀⠀⠀⠀⠀⢀⣴⡿⠁
⠀⢀⣴⣿⣿⣿⣟⣁⣀⣀⣤⠔⢒⣿⣿⣿⣿⠿⣍⡀⠉⠻⣶⡆⠀⠘⣿⣷⣄⠀⠀⠀⣀⣴⠿⠋⠀⠀
⢠⡾⠋⠁⠀⢹⣿⡿⠋⣡⣏⠤⠋⣱⡿⢻⡟⡓⢦⣽⣦⣴⣿⣧⠂⢠⡏⠙⠻⢿⣿⣿⠟⠁⠀⠀⠀⠀
⣿⣧⣤⣤⣤⣾⡯⠤⠚⠋⠁⠀⢰⠟⠀⡞⢀⡇⠈⢿⡟⠯⣭⣤⣴⣋⣠⡤⠶⠛⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⣧⠊⣧⠀⢸⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⣰⣿⣧⣸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⡿⠟⠻⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⢸⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣄⣠⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''

# Получаем ввод пользователя
str_var = input("Введите строку: ")
# Готовим новую строку
new_str = ""
for i in str_var:
    # Меняем регистры
    if i.isupper():
        new_str += i.lower()
    else:
        new_str += i.upper()
# Выводим новую строку
print(new_str)

'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⡿⠻⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣿⠁⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⡇⠀⠀⠀⠀⠹⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⣿⡇⠀⠀⠀⠀⠀⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡟⣿⣦⣀⠀⣀⣼⠁⣿⣿⠀⠲⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡇⠈⢛⣿⠿⢿⣿⡄⠘⢻⡇⠀⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⡇⣴⠋⠀⠀⣀⠈⠙⣄⠈⡇⠀⢰⠀⣀⠤⠐⠶⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠹⣇⢰⣷⣾⠷⢶⣤⡘⣤⠇⠀⠞⠋⠀⠀⣀⣠⣤⣴⣶⣶⣶⣶⣦⣤⣀⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⣿⣧⣄⡀⠙⣿⣿⣠⡟⢀⡤⠒⠉⠉⠉⠉⠛⣫⠟⠋⠉⠉⠉⠛⠻⢿⣶⣄
⠀⠀⠀⢀⣤⣶⣾⣿⣿⠶⠿⠿⢦⣙⣦⣿⣿⣿⣾⣟⣉⡉⠉⠙⠶⣶⣿⡇⠀⠀⠀⠀⠀⠀⢀⣴⡿⠁
⠀⢀⣴⣿⣿⣿⣟⣁⣀⣀⣤⠔⢒⣿⣿⣿⣿⠿⣍⡀⠉⠻⣶⡆⠀⠘⣿⣷⣄⠀⠀⠀⣀⣴⠿⠋⠀⠀
⢠⡾⠋⠁⠀⢹⣿⡿⠋⣡⣏⠤⠋⣱⡿⢻⡟⡓⢦⣽⣦⣴⣿⣧⠂⢠⡏⠙⠻⢿⣿⣿⠟⠁⠀⠀⠀⠀
⣿⣧⣤⣤⣤⣾⡯⠤⠚⠋⠁⠀⢰⠟⠀⡞⢀⡇⠈⢿⡟⠯⣭⣤⣴⣋⣠⡤⠶⠛⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⣧⠊⣧⠀⢸⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⣰⣿⣧⣸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⡿⠟⠻⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⢸⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣄⣠⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''

import random as r
import string as s

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
    print(f"Изначальный массив: \n{array[0]}\n{array[1]}\n{array[2]}\n{array[3]}\n{array[4]}")

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
    print(f"Обнулённый массив: \n{array[0]}\n{array[1]}\n{array[2]}\n{array[3]}\n{array[4]}")
    
create_array()

'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⡿⠻⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣿⠁⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⡇⠀⠀⠀⠀⠹⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⣿⡇⠀⠀⠀⠀⠀⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡟⣿⣦⣀⠀⣀⣼⠁⣿⣿⠀⠲⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡇⠈⢛⣿⠿⢿⣿⡄⠘⢻⡇⠀⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⡇⣴⠋⠀⠀⣀⠈⠙⣄⠈⡇⠀⢰⠀⣀⠤⠐⠶⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠹⣇⢰⣷⣾⠷⢶⣤⡘⣤⠇⠀⠞⠋⠀⠀⣀⣠⣤⣴⣶⣶⣶⣶⣦⣤⣀⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⣿⣧⣄⡀⠙⣿⣿⣠⡟⢀⡤⠒⠉⠉⠉⠉⠛⣫⠟⠋⠉⠉⠉⠛⠻⢿⣶⣄
⠀⠀⠀⢀⣤⣶⣾⣿⣿⠶⠿⠿⢦⣙⣦⣿⣿⣿⣾⣟⣉⡉⠉⠙⠶⣶⣿⡇⠀⠀⠀⠀⠀⠀⢀⣴⡿⠁
⠀⢀⣴⣿⣿⣿⣟⣁⣀⣀⣤⠔⢒⣿⣿⣿⣿⠿⣍⡀⠉⠻⣶⡆⠀⠘⣿⣷⣄⠀⠀⠀⣀⣴⠿⠋⠀⠀
⢠⡾⠋⠁⠀⢹⣿⡿⠋⣡⣏⠤⠋⣱⡿⢻⡟⡓⢦⣽⣦⣴⣿⣧⠂⢠⡏⠙⠻⢿⣿⣿⠟⠁⠀⠀⠀⠀
⣿⣧⣤⣤⣤⣾⡯⠤⠚⠋⠁⠀⢰⠟⠀⡞⢀⡇⠈⢿⡟⠯⣭⣤⣴⣋⣠⡤⠶⠛⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⣧⠊⣧⠀⢸⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⣰⣿⣧⣸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⡿⠟⠻⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⢸⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣄⣠⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''

# Переменная для принятия ввода от пользователя
user_inp = input("Введите строку: ")

# Заранее заготовленный список гласных в русском и английском языках
vowels = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я", "a", "e", "i", "o", "u"]

# Приводим всё к единому формату (все буквы маленькие)
str_var = user_inp.lower()
# Создаём счётчик букв и считаем только те, что есть в нашем готовом листе
vowels_cnt = 0
for i in str_var:
    if i in vowels:
        vowels_cnt += 1

# Меняем текст на получившееся количество букв
print(f"Гласных: {vowels_cnt}")

'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⡿⠻⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣿⠁⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⡇⠀⠀⠀⠀⠹⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⣿⡇⠀⠀⠀⠀⠀⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡟⣿⣦⣀⠀⣀⣼⠁⣿⣿⠀⠲⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡇⠈⢛⣿⠿⢿⣿⡄⠘⢻⡇⠀⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⡇⣴⠋⠀⠀⣀⠈⠙⣄⠈⡇⠀⢰⠀⣀⠤⠐⠶⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠹⣇⢰⣷⣾⠷⢶⣤⡘⣤⠇⠀⠞⠋⠀⠀⣀⣠⣤⣴⣶⣶⣶⣶⣦⣤⣀⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⣿⣧⣄⡀⠙⣿⣿⣠⡟⢀⡤⠒⠉⠉⠉⠉⠛⣫⠟⠋⠉⠉⠉⠛⠻⢿⣶⣄
⠀⠀⠀⢀⣤⣶⣾⣿⣿⠶⠿⠿⢦⣙⣦⣿⣿⣿⣾⣟⣉⡉⠉⠙⠶⣶⣿⡇⠀⠀⠀⠀⠀⠀⢀⣴⡿⠁
⠀⢀⣴⣿⣿⣿⣟⣁⣀⣀⣤⠔⢒⣿⣿⣿⣿⠿⣍⡀⠉⠻⣶⡆⠀⠘⣿⣷⣄⠀⠀⠀⣀⣴⠿⠋⠀⠀
⢠⡾⠋⠁⠀⢹⣿⡿⠋⣡⣏⠤⠋⣱⡿⢻⡟⡓⢦⣽⣦⣴⣿⣧⠂⢠⡏⠙⠻⢿⣿⣿⠟⠁⠀⠀⠀⠀
⣿⣧⣤⣤⣤⣾⡯⠤⠚⠋⠁⠀⢰⠟⠀⡞⢀⡇⠈⢿⡟⠯⣭⣤⣴⣋⣠⡤⠶⠛⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⣧⠊⣧⠀⢸⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⣰⣿⣧⣸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⡿⠟⠻⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⢸⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣄⣠⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''

import numpy as np
import matplotlib.pyplot as plt

# Записали неравенства (Вариант №70)
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
print(f'Всего точек: {cnt}')

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


'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⡿⠻⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣿⠁⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⡇⠀⠀⠀⠀⠹⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⣿⡇⠀⠀⠀⠀⠀⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡟⣿⣦⣀⠀⣀⣼⠁⣿⣿⠀⠲⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡇⠈⢛⣿⠿⢿⣿⡄⠘⢻⡇⠀⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⡇⣴⠋⠀⠀⣀⠈⠙⣄⠈⡇⠀⢰⠀⣀⠤⠐⠶⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠹⣇⢰⣷⣾⠷⢶⣤⡘⣤⠇⠀⠞⠋⠀⠀⣀⣠⣤⣴⣶⣶⣶⣶⣦⣤⣀⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⣿⣧⣄⡀⠙⣿⣿⣠⡟⢀⡤⠒⠉⠉⠉⠉⠛⣫⠟⠋⠉⠉⠉⠛⠻⢿⣶⣄
⠀⠀⠀⢀⣤⣶⣾⣿⣿⠶⠿⠿⢦⣙⣦⣿⣿⣿⣾⣟⣉⡉⠉⠙⠶⣶⣿⡇⠀⠀⠀⠀⠀⠀⢀⣴⡿⠁
⠀⢀⣴⣿⣿⣿⣟⣁⣀⣀⣤⠔⢒⣿⣿⣿⣿⠿⣍⡀⠉⠻⣶⡆⠀⠘⣿⣷⣄⠀⠀⠀⣀⣴⠿⠋⠀⠀
⢠⡾⠋⠁⠀⢹⣿⡿⠋⣡⣏⠤⠋⣱⡿⢻⡟⡓⢦⣽⣦⣴⣿⣧⠂⢠⡏⠙⠻⢿⣿⣿⠟⠁⠀⠀⠀⠀
⣿⣧⣤⣤⣤⣾⡯⠤⠚⠋⠁⠀⢰⠟⠀⡞⢀⡇⠈⢿⡟⠯⣭⣤⣴⣋⣠⡤⠶⠛⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⣧⠊⣧⠀⢸⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⣰⣿⣧⣸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⡿⠟⠻⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⢸⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣄⣠⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''

import re

# Задание 8_1
print('С помощью регулярных выражений уберите все символы пунктуации из предложения')
def punctuation():
    inp = '''A, very very; irregular_sentence'''
    # Не оставляет пробел вместо знаков "_", но я и не думаю, что это возможно, да и нужно
    new_str = re.sub(r'[^\w\s]|_', '', inp)
    print(new_str)

punctuation()
    


# Задание 8_2
print('Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).')
def tandem():
    inp = '''blabla is a tandem repetition
            123123 is good too
            go go
            aaa
            '''
    pattern = r'\b(\w+)\1\b'
    new_str = [line for line in inp.split('\n') if re.search(pattern, line)]
    for item in new_str:
        print(item)

tandem()

# Задание 8_3
print('Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.')
def print_cat_cat():
    inp = '''catcat
            cat and cat
            catac
            cat
            ccaatt
            '''
    new_str = "\n".join(re.findall(r'(cat.*cat)', inp, re.MULTILINE)) 
    print(new_str)

print_cat_cat()

# Задание 8_4
print('Выведите строки, содержащие "cat" в качестве слова.')
def print_cat():
    inp = '''cat
            catapult and cat
            catcat
            concat
            Cat
            "cat"
            !cat?
            '''
    new_str = "\n".join(re.findall(r'(^.*\bcat\b.*$)', inp, re.MULTILINE)) 
    print(new_str)

print_cat()

# Задание 8_5
print('Выведите строки, содержащие обратный слеш "\\".')
def print_backslash():
    inp = '''\w denotes word character
            No slashes here
            '''
    new_str = "\n".join(re.findall(r'.*\\.*', inp, re.MULTILINE)) 
    print(new_str)

print_backslash()

# Задание 8_6
print("В каждой строке замените все вхождения подстроки \"human\" на подстроку \"computer\" и выведите полученные строки.")
def change_to_computer():
    inp = '''I need to understand the human mind
            humanity
            '''
    new_str = re.sub(r'human', 'computer', inp)
    print(new_str)

change_to_computer()


# Задание 8_7
print("В каждой строке замените первое вхождение слова, состоящего только из латинских букв \"a\" (регистр не важен), на слово \"argh\".")
def change_to_argh():
    inp = '''There’ll be no more "Aaaaaaaaaaaaaaa"
            AaAaAaA AaAaAaA
            '''
    new_str = re.sub(r'\b[aA]+\b', 'argh', inp, count=1)
    print(new_str)

change_to_argh()


# Задание 8_8
print("В каждой строке поменяйте местами две первые буквы каждого слова, состоящего хотя бы из двух букв.")
def swap_two_first_letters():
    inp = '''this is a text
            "this' !is. ?n1ce,
            '''
    
    def swap(found):
        word = found.group()
        return word[1] + word[0] + word[2:]
    
    new_str = re.sub(r"\w[a-zA-Z0-9а-яА-Я]{1,}", swap, inp)
    print(new_str)

swap_two_first_letters()


# Задание 8_9
print("В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.")
def several_letters_to_one():
    inp = '''attraction
            buzzzz
            '''
    new_str = re.sub(r"([a-zA-Z0-9а-яА-Я])\1{1,}", r"\1", inp)
    print(new_str)

several_letters_to_one()


# Задание 8_10
print("Извлеките никнейм пользователя, имя домена и суффикс из данных email адресов")
def email_work():
    inp = '''emails = """zuck26@facebook.com              # Многострочный комментарий
            page33@google.com  
            jeff42@amazon.com"""  
            '''
    pattern = r'(\w+)@(\w+)\.(\w+)'
    new_str = re.findall(pattern, inp)
    for item in new_str:
        print(item)
    
email_work()

'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⡿⠻⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣿⠁⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⡇⠀⠀⠀⠀⠹⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⣿⡇⠀⠀⠀⠀⠀⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡟⣿⣦⣀⠀⣀⣼⠁⣿⣿⠀⠲⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡇⠈⢛⣿⠿⢿⣿⡄⠘⢻⡇⠀⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⡇⣴⠋⠀⠀⣀⠈⠙⣄⠈⡇⠀⢰⠀⣀⠤⠐⠶⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠹⣇⢰⣷⣾⠷⢶⣤⡘⣤⠇⠀⠞⠋⠀⠀⣀⣠⣤⣴⣶⣶⣶⣶⣦⣤⣀⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⣿⣧⣄⡀⠙⣿⣿⣠⡟⢀⡤⠒⠉⠉⠉⠉⠛⣫⠟⠋⠉⠉⠉⠛⠻⢿⣶⣄
⠀⠀⠀⢀⣤⣶⣾⣿⣿⠶⠿⠿⢦⣙⣦⣿⣿⣿⣾⣟⣉⡉⠉⠙⠶⣶⣿⡇⠀⠀⠀⠀⠀⠀⢀⣴⡿⠁
⠀⢀⣴⣿⣿⣿⣟⣁⣀⣀⣤⠔⢒⣿⣿⣿⣿⠿⣍⡀⠉⠻⣶⡆⠀⠘⣿⣷⣄⠀⠀⠀⣀⣴⠿⠋⠀⠀
⢠⡾⠋⠁⠀⢹⣿⡿⠋⣡⣏⠤⠋⣱⡿⢻⡟⡓⢦⣽⣦⣴⣿⣧⠂⢠⡏⠙⠻⢿⣿⣿⠟⠁⠀⠀⠀⠀
⣿⣧⣤⣤⣤⣾⡯⠤⠚⠋⠁⠀⢰⠟⠀⡞⢀⡇⠈⢿⡟⠯⣭⣤⣴⣋⣠⡤⠶⠛⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⣧⠊⣧⠀⢸⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⣰⣿⣧⣸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⡿⠟⠻⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⢸⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣄⣠⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''

import re

# Создаём паттерны по которым будем вычислять в тексте нужные элементы
name_pattern = r'[А-ЯЁ][а-яё]+\s[А-ЯЁ]\.[А-ЯЁ]\.'
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
phone_pattern = r'\+7\(\d{3}\)\d{3}-\d{2}-\d{2}'

def extract():
    text = '''студент Петров В.П. - группа УМР11 тел. +7(918)240-04-40
# Email: petrov@mail.ru доп. тел +7(926)718-33-22'''
    # Ищем по паттернам нужные элементы
    fio = re.search(name_pattern, text).group()
    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)
    # Меняем текст, выводим результат
    print(f'ФИО: {fio} \nEmail: {emails} \nТелефон: {phones} ')

extract()

