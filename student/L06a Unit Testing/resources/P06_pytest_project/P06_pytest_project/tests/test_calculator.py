from calculator.calculator import Calculator
import pytest

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected





    def test_subtract(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 3087
        assert result == expected


    def test_multiply(self):
        # arrange
        a = 4
        b = 1
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 4
        assert result == expected

    def test_divide(self):
        # arrange
        a = 4
        b = 1
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 4
        assert result == expected



    def test_divide2(self):
        # arrange
        a = 4
        b = 0
        cal = Calculator()

        # act and assert
        with pytest.raises(ZeroDivisionError):
            cal.divide(a,b)