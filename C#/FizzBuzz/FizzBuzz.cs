namespace FizzBuzzKata
{
    public class FizzBuzzKata
    {
        public FizzBuzzKata()
        {
        }

        private Dictionary<int,string> Rules = new Dictionary<int,string>()
        {
            {15, "FizzBuzz"},
            {3, "Fizz"},
            {5, "Buzz"},
        };

        public string FizzBuzz(int number)
        {
            foreach(var key in Rules.Keys)
            {
                if(number % key == 0)
                {
                    return Rules[key];
                }
            }
            return number.ToString();
        }
    }
}