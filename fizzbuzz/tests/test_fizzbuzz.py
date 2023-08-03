import pytest

from src.fizzbuzz import FizzBuzz


class TestFizzBuzz:

    @pytest.mark.parametrize("test_input,expected",
                             [(1, "1"), (2, "2"), (3, "Fizz"),
                              (4, "4"), (5, "Buzz"), (6, "Fizz"),
                              (7, "7"), (8, "8"), (9, "Fizz"),
                              (10, "Buzz"), (12, "Fizz"), (20, "Buzz")
                              ]
                             )
    def test_valid_output_is_returned(self, test_input, expected):

        fizzbuzz_processor = FizzBuzz()
        assert expected == fizzbuzz_processor.process(test_input)

    def test_fizzbuzz_is_returned(self):

        fizzbuzz_processor = FizzBuzz()
        assert "FizzBuzz" == fizzbuzz_processor.process(15)

    def test_30_then_fizzbuzz_is_returned(self):

        fizzbuzz_processor = FizzBuzz()
        assert "FizzBuzz" == fizzbuzz_processor.process(30)

    def test_45_then_fizzbuzz_is_returned(self):

        fizzbuzz_processor = FizzBuzz()
        assert "FizzBuzz" == fizzbuzz_processor.process(45)




