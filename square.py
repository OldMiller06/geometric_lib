import unittest
def area(a):
    '''
    Принимает длину стороны квадрата и возвращает его площадь

    Параметры:
        a (float): Сторона квадрата

    Возвращаемое значение:
        area (float): Площадь квадрата
    '''

    return a * a


def perimeter(a):
    '''
    Принимает длину стороны квадрата и возвращает его периметр

    Параметры:
        a (float): Сторона квадрата

    Возвращаемое значение:
        perimeter (float): Площадь периметр 
    '''

    return 4 * a

class TestSquareFunctions(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(2), 4)
        self.assertEqual(area(0), 0)
        self.assertEqual(area(5.5), 30.25)
        self.assertEqual(area(1), 1)
        self.assertEqual(area(10), 100)
        self.assertAlmostEqual(area(0.1), 0.01)
        self.assertAlmostEqual(area(3.3), 10.89)
        self.assertEqual(area(-2), 4)
        self.assertAlmostEqual(area(-3.5), 12.25)
        self.assertEqual(area(1000), 1000000)
        self.assertEqual(area(1000), area(1000))

    def test_perimeter(self):
        self.assertEqual(perimeter(2), 8)
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(5.5), 22)
        self.assertEqual(perimeter(1), 4)
        self.assertEqual(perimeter(10), 40)
        self.assertAlmostEqual(perimeter(0.1), 0.4)
        self.assertAlmostEqual(perimeter(3.3), 13.2)
        self.assertEqual(perimeter(-2), -8)
        self.assertAlmostEqual(perimeter(-3.5), -14)
        self.assertEqual(perimeter(1000), 4000)
        
if __name__ == '__main__':
    unittest.main()