from src.fizzbuzz import FizzBuzz


class TestFizzBuzz:

    def test_first_number_is_returned(self):

        fizzbuzz_processor = FizzBuzz()
        assert "1" == fizzbuzz_processor.process(1)

    def test_second_number_is_returned(self):
        fizzbuzz_processor = FizzBuzz()
        assert "2" == fizzbuzz_processor.process(2)

    def test_fourth_number_is_returned(self):
        fizzbuzz_processor = FizzBuzz()
        assert "4" == fizzbuzz_processor.process(4)

