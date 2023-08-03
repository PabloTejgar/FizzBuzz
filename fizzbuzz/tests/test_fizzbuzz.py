import pytest

from src.fizzbuzz import FizzBuzz


class TestFizzBuzz:

    @pytest.mark.parametrize("test_input,expected", [(1, "1"), (2, "2"), (4, "4")])
    def test_number_is_returned(self, test_input, expected):

        fizzbuzz_processor = FizzBuzz()
        assert expected == fizzbuzz_processor.process(test_input)

    def test_three_provided_then_fizz_returned(self):

        fizzbuzz_processor = FizzBuzz()
        assert "Fizz" == fizzbuzz_processor.process(3)




