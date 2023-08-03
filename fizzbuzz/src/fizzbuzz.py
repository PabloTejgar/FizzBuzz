class FizzBuzz:

    def process(self, number: int):
        if number % 3 == 0:
            return "Fizz"
        if number % 5 == 0:
            return "Buzz"

        return str(number)
