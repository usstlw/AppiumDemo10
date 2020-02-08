from unittest import TestCase
from ddt import ddt,data,file_data,unpack
import yaml
from src.calc import Calc

@ddt
class TestCalc(TestCase):

    def setUpClass(cls) -> None:
        self.calc=Calc()
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
        print(a,b,c)
        result=self.calc.add(a,b)
        # print("result="+str(result))
        # assert  result == 2
        print(a,b,c)
        self.assertEqual(self.calc.add(a,b),c)


    @file_data("calc.yaml")
    def test_div(self,a,b,c):
        calc=Calc()
        print(a,b,c)
        self.assertEqual(calc.div(a,b),c)

        # result=calc.div(1,2)
        # self.assertEqual(result,0.5)
        #
        # result=calc.div(100,100)
        # self.assertEqual(result,1)