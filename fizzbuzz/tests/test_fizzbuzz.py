import pytest

from src.fizzbuzz import FizzBuzz


class TestFizzBuzz:

    @pytest.mark.parametrize("test_input,expected",
                             [(1, "1"), (2, "2"), (4, "4"), (7, "7"),
                              (3, "Fizz"), (6, "Fizz"), (9, "Fizz"), (12, "Fizz"),
                              (5, "Buzz"), (10, "Buzz"),  (20, "Buzz"), (25, "Buzz"),
                              (15, "FizzBuzz"), (30, "FizzBuzz"), (45, "FizzBuzz"), (60, "FizzBuzz")
                              ]
                             )
    def test_valid_output_is_returned(self, test_input, expected):

        fizzbuzz_processor = FizzBuzz()
        assert expected == fizzbuzz_processor.process(test_input)





