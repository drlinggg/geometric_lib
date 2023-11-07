import unittest
import circle
import rectangle
import square
import triangle

class MyTestCase(unittest.TestCase):

    def test_rectangle_mul_by_positive(self):
        self.assertEqual(rectangle.area(10,10),100)
        self.assertEqual(rectangle.area(10,5),50)
        self.assertEqual(rectangle.area(5,10),50)

    def test_rectangle_area_mult_by_non_positive(self):
        self.assertEqual(rectangle.area(10,0),-1)
        self.assertEqual(rectangle.area(0,0),-1)
        self.assertEqual(rectangle.area(0,10),-1)

    def test_rectangle_perimeter_addition_by_positive(self):
        self.assertEqual(rectangle.perimeter(5,5), 20)
        self.assertEqual(rectangle.perimeter(7,3),20)
        self.assertEqual(rectangle.perimeter(3, 7), 20)


    def test_rectangle_repimeter_addition_by_non_positive(self):
        self.assertEqual(rectangle.perimeter(0, 0), -1)
        self.assertEqual(rectangle.perimeter(0,5),-1)
        self.assertEqual(rectangle.perimeter(5, 0), -1)
        self.assertEqual(rectangle.perimeter(-5,5), -1)
        self.assertEqual(rectangle.perimeter(5, -5), -1)

    def test_circle_perimeter_by_positive(self):
        self.assertEqual(circle.perimeter(1), 6.283185307179586)


    def test_circle_perimeter_by_non_positive(self):
        self.assertEqual(circle.perimeter(0), -1)
        self.assertEqual(circle.perimeter(-1), -1)


    def test_circle_area_by_positive(self):
        self.assertEqual(circle.area(1),3.141592653589793)


    def test_circle_area_by_non_positive(self):
        self.assertEqual(circle.area(0),-1)
        self.assertEqual(circle.area(-1),-1)


    def test_square_perimeter_by_positive(self):
        self.assertEqual(square.perimeter(5),20)
        self.assertEqual(square.perimeter(10), 40)


    def test_square_perimeter_by_non_positive(self):
        self.assertEqual(square.perimeter(0),-1)
        self.assertEqual(square.perimeter(-1), -1)


    def test_square_area_by_non_positive(self):
        self.assertEqual(square.area(0),-1)
        self.assertEqual(square.area(-1), -1)


    def test_square_area_by_positive(self):
        self.assertEqual(square.perimeter(5),20)
        self.assertEqual(square.perimeter(4), 16)


    def test_triangle_perimeter_by_positive(self):
        self.assertEqual(triangle.perimeter(3,3,3),9)
        self.assertEqual(triangle.perimeter(4, 3, 5), 12)

    def test_triangle_perimeter_by_non_positive(self):
        self.assertEqual(triangle.perimeter(-1, 3, 3), -1)
        self.assertEqual(triangle.perimeter(3, -1, 3), -1)
        self.assertEqual(triangle.perimeter(3, 3, -1), -1)
        self.assertEqual(triangle.perimeter(0, 3, 3), -1)
        self.assertEqual(triangle.perimeter(3, 0, 3), -1)
        self.assertEqual(triangle.perimeter(3, 3, 0), -1)

    def test_triangle_area_by_positive(self):
        self.assertEqual(triangle.area(3, 2), 3)
        self.assertEqual(triangle.area(2, 3), 3)

    def test_triangle_area_by_non_positive(self):
        self.assertEqual(triangle.area(0,2), -1)
        self.assertEqual(triangle.area(2, 0), -1)
        self.assertEqual(triangle.area(-1, 2), -1)
        self.assertEqual(triangle.area(2,-1), -1)
        self.assertEqual(triangle.area(0, 0), -1)


if __name__ == '__main__':
    unittest.main()
