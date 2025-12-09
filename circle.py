import math, unittest

def area(r):
    '''
    Принимает радиус окружности и возвращает её площадь

    Параметр:
        r (float): Радиус окружности
    
    Возвращаемое значение:
        area (float): Площадь окружности
    '''

    return math.pi * r * r


def perimeter(r):
    '''
    Принимает радиус окружности и возвращает её периметр
    
    Параметр: r (float): Радиус окружности

    Возвращаемое значение:
        perimeter (float): Периметр окружности
    '''

    return 2 * math.pi * r

class TestCircle(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(1), math.pi)
        self.assertAlmostEqual(area(0), 0)
        self.assertNotEqual(area(2), 10)
        self.assertAlmostEqual(area(3), 28.274333882308138)
        self.assertAlmostEqual(area(1.5), 7.0685834705770345)
        self.assertAlmostEqual(area(2.5), 19.634954084936208)
        self.assertNotEqual(area(4), 50)
        self.assertAlmostEqual(area(0.5), 0.7853981633974483)
        self.assertAlmostEqual(area(5), 78.53981633974483)
        self.assertNotEqual(area(3), 30)

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(perimeter(0), 0)
        self.assertNotEqual(perimeter(2), 10)
        self.assertAlmostEqual(perimeter(3), 18.84955592153876)
        self.assertAlmostEqual(perimeter(1.5), 9.42477796076938)
        self.assertAlmostEqual(perimeter(2.5), 15.707963267948966)
        self.assertNotEqual(perimeter(4), 20)
        self.assertAlmostEqual(perimeter(0.5), 3.141592653589793)
        self.assertAlmostEqual(perimeter(5), 31.41592653589793)
        self.assertNotEqual(perimeter(3), 20)

if __name__ == "__main__":
    unittest.main()