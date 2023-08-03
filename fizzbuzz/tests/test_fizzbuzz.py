from src.fizzbuzz import FizzBuzz


class TestFizzBuzz:

    def test_first_number_is_returned(self):

        fizzbuzz_processor = FizzBuzz()
        assert "1" == fizzbuzz_processor.process(1)

    def test_second_number_is_returned(self):
        fizzbuzz_processor = FizzBuzz()
        assert "2" == fizzbuzz_processor.process(2)

