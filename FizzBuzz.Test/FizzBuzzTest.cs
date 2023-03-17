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

    }
}