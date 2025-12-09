import unittest
def area(a, h):
    '''
    Принимает основание и высоту треугольника и возвращает его площадь

    Параметры:
        a (float): Основание треугольника
        h (float): Высота треугольника

    Возвращаемое значение:
        area (float): Площадь треугольника
    '''

    return a * h / 2

def perimeter(a, b, c):
    '''
    Принимает три стороны треугольника и возвращает его периметр

    Параметры:
        a (float): Первая сторона треугольника
        b (float): Вторая сторона треугольника
        c (float): Третья сторона треугольника

    Возвращаемое значение:
        perimeter (float): Периметр треугольника
    '''
    
    return a + b + c
class TestTriangleFunctions(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(2, 3), 3)
        self.assertEqual(area(5, 0), 0)
        self.assertEqual(area(0, 10), 0)
        self.assertAlmostEqual(area(2.5, 4.2), 5.25)
        self.assertEqual(area(1000, 2000), 1000000)
        self.assertEqual(area(-2, 3), -3)
        self.assertEqual(area(2, -3), -3)
        self.assertEqual(area(-4, -5), 10)
        self.assertAlmostEqual(area(0.1, 0.2), 0.01)
        self.assertGreater(area(5, 10), area(5, 5))


    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(0, 4, 5), 9)
        self.assertEqual(perimeter(0, 0, 0), 0)
        self.assertAlmostEqual(perimeter(1.5, 2.5, 3.5), 7.5)
        self.assertEqual(perimeter(1000, 2000, 3000), 6000)
        self.assertEqual(perimeter(-2, 5, 6), 9)
        self.assertAlmostEqual(perimeter(0.1, 0.2, 0.3), 0.6)
        self.assertGreater(perimeter(5, 5, 5), 0)
        self.assertLess(perimeter(3, 4, 5), perimeter(3, 4, 6))
        self.assertEqual(perimeter(-3, -4, -5), -12)

if __name__ == "__main__":
    unittest.main()