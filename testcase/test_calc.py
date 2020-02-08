from unittest import TestCase
from ddt import ddt,data,file_data,unpack
from src.calc import Calc

@ddt
class TestCalc(TestCase):
    @data(1,2,3,4,5,6)
    def test_demo(self,real):
        self.assertEqual(real,5)

    @data((1,1,2),
          (1,0,1),
          (1,-1,0),
          (1,1000000,1000001)
          )
    @unpack
    def test_add(self,a,b,c):
        calc=Calc()
        result=calc.add(a,b)
        # assert  result == 2
        self.assertEqual(result,c)


    def test_div(self):
        calc=Calc()
        result=calc.div(2,1)
        self.assertEqual(result,2)

        result=calc.div(1,2)
        self.assertEqual(result,0.5)

        result=calc.div(100,100)
        self.assertEqual(result,1)