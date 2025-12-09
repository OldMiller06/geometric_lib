import unittest
def area(a, b):
    '''
    Принимает две перпендикулярные стороны прямоугольника и возвращает его площадь

    Параметры:
        a (float): Первая сторона прямоугольника
        b (float): Вторая сторона прямоугольника

    Возвращаемое значение:
        area (float): Площадь прямоугольника 
    '''
    return a * b

def perimeter(a, b):
    '''
    Принимает две перпендикулярные стороны прямоугольника и возвращает его периметр

    Параметры:
        a (float): Первая сторона прямоугольника
        b (float): Вторая сторона прямоугольника

    Возвращаемое значение:
        perimeter (float): Периметр прямоугольника 
    '''

    return 2*a + 2*b

class TestRectangleFunctions(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(3, 4), 12)
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(0, 0), 0)
        self.assertAlmostEqual(area(2.5, 4.2), 10.5)
        self.assertEqual(area(1000, 2000), 2000000)
        self.assertEqual(area(-2, 5), -10)
        self.assertEqual(area(-3, -4), 12)
        self.assertAlmostEqual(area(0.1, 0.2), 0.02)
        self.assertEqual(area(3, 7), area(7, 3))
        self.assertAlmostEqual(area(14, 8), 112.0)


    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4), 14)
        self.assertEqual(perimeter(0, 5), 10)
        self.assertEqual(perimeter(0, 0), 0)
        self.assertAlmostEqual(perimeter(2.5, 4.2), 13.4)
        self.assertEqual(perimeter(1000, 2000), 6000)
        self.assertEqual(perimeter(-2, 5), 6)
        self.assertEqual(perimeter(-3, -4), -14)
        self.assertAlmostEqual(perimeter(0.1, 0.2), 0.6)
        self.assertLess(perimeter(3, 4), perimeter(4, 4))
        self.assertAlmostEqual(perimeter(14, 8), 44.0)

if __name__ == "__main__":
    unittest.main()