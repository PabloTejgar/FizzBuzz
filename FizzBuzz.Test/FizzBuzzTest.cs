using NUnit.Framework;

namespace FizzBuzz.Test
{
    public class FizzBuzzTest
    {
        [Test]
        [TestCase(1,"1")]
        [TestCase(2, "1")]
        [TestCase(4, "1")]
        public void AddANonMultipleReturnsTheNumber()
        {
            var generator = new FizzBuzz();
            Assert.AreEqual(generator.FizzBuzz(input), expected);
        }

    }
}