using NUnit.Framework;

namespace FizzBuzzKata.Test
{
    public class FizzBuzzTest
    {
        [Test]
        [TestCase(1,"1")]
        [TestCase(2, "2")]
        [TestCase(4, "4")]
        public void AddANonMultipleReturnsTheNumber(int input, string expected)
        {
            var generator = new FizzBuzzKata();
            Assert.AreEqual(generator.FizzBuzz(input), expected);
        }

        [Test]
        [TestCase(3, "Fizz")]
        [TestCase(6, "Fizz")]
        [TestCase(9, "Fizz")]
        public void AddMultiple3ReturnsFizz(int input, string expected)
        {
            var generator = new FizzBuzzKata();
            Assert.AreEqual(generator.FizzBuzz(input), expected);
        }


        [Test]
        [TestCase(5, "Buzz")]
        [TestCase(10, "Buzz")]
        [TestCase(20, "Buzz")]
        public void AddMultiple5ReturnsBuzz(int input, string expected)
        {
            var generator = new FizzBuzzKata();
            Assert.AreEqual(generator.FizzBuzz(input), expected);
        }


    }
}