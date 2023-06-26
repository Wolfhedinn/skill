import  pytest

from app.calc import Caalculator

class TestCalc:
    def setup(self):
        self.calc = Caalculator

        def test_adding_success(self):
            assert self.calc.adding(self,1,1) == 2

         def test_zero_division(self):
             with pytest. raises(ZeroDivisionError):
                 self.calc.division(self,1,0)

         def teardown(self):
             print('Выполнение метода Teardown')