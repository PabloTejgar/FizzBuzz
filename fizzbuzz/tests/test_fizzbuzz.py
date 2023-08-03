import pytest

from src.fizzbuzz import FizzBuzz


class TestFizzBuzz:

    @pytest.mark.parametrize("test_input,expected", [(1, "1"), (2, "2"), (4, "4")])
    def test_number_is_returned(self, test_input, expected):

        fizzbuzz_processor = FizzBuzz()
        assert expected == fizzbuzz_processor.process(test_input)

    @pytest.mark.parametrize("test_input,expected", [(3, "Fizz"), (6, "Fizz"), (9, "Fizz"), (12, "Fizz")])

    def test_multiple_of_three_provided_then_fizz_returned(self, test_input, expected):

        fizzbuzz_processor = FizzBuzz()
        assert expected == fizzbuzz_processor.process(test_input)

    @pytest.mark.parametrize("test_input,expected", [(5, "Buzz"), (10, "Buzz"), (20, "Buzz"), (25, "Buzz")])

    def test_multiple_of_five_provided_then_buzz_returned(self, test_input, expected):

        fizzbuzz_processor = FizzBuzz()
        assert expected == fizzbuzz_processor.process(test_input)



