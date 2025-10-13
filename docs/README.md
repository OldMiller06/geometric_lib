# geometric_lib

## Общее описание решения

В этом репозитории содержатся 4 модуля, каждый для своей фигуры.
Внутри 2 функции: **Нахождение площади** и **Нахождение периметра**


| Файл | Назначение |
|------|-------------|
| `rectangle.py` | Функции для вычисления площади и периметра прямоугольника |
| `triangle.py`  | Функции для вычисления площади и периметра треугольника |
| `square.py`    | Функции для вычисления площади и периметра квадрата |
| `circle.py`    | Функции для вычисления площади и длины окружности круга |

---

## Описание функций и их примеры

### circle.py
```python
from circle import area, perimeter
circle_area = area(2)
print(circle_area) # Вывод: 12.566370614359172

circle_perimeter = area(2)
print(circle_perimeter) # Вывод: 12.566370614359172
```

### rectangle.py
```python
from rectangle import area, perimeter
rectangle_area = area(2, 3)
print(rectangle_area) # Вывод: 6.0

rectangle_perimeter = area(2, 3)
print(rectangle_perimeter) # Вывод: 10.0
```

### triangle.py
```python
from triangle import area, perimeter
triangle_area = area(2, 3)
print(triangle_area) # Вывод: 3.0

triangle_perimeter = area(1, 2, 3)
print(triangle_perimeter) # Вывод: 6.0
```

### square.py
```python
from square import area, perimeter
square_area = area(2)
print(square_area) # Вывод: 4.0

square_perimeter = area(2)
print(square_perimeter) # Вывод: 8.0
```
---

## История коммитов
1.  8ba9aeb3cea847b63a91ac378a2a6db758682460 - L-03: Circle and square added
2.  d078c8d9ee6155f3cb0e577d28d337b791de28e2 - L-03: Docs added
3.  70fa0c2f36b77cf9d78d09900ce4442f7799c49a - Added new files: triangle.py, rectangle.py
4.  b5310d62d4110745c4be09ece16cfc7e87fed41b - Added comments to every function