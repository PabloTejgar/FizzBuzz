namespace FizzBuzzKata
{
    public class FizzBuzzKata
    {
        public FizzBuzzKata()
        {
        }

        public string FizzBuzz(int number)
        {
            if(number % 3 == 0)
            {
                return "Fizz";
            }
            if (number % 5 == 0)
            {
                return "Buzz";
            }
            return number.ToString();
        }
    }
}