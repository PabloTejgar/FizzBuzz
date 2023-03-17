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
            return number.ToString();
        }
    }
}