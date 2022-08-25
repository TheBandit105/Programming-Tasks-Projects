using System;

namespace Decisions
{
    class Program
    {
        static void Main(string[] args)
        {
            /*
            Console.WriteLine("Please enter something and press the enter key: ");
            string userValue = Console.ReadLine();
            Console.WriteLine("You typed: " + userValue);
            */

            Console.WriteLine("Choose a numbered door from 1 to 3: ");
            string userValue = Console.ReadLine();

            string message = "";

            if (userValue == "1")
            {
                message = "Congratulations! You've won a new car!";
            }
            else if (userValue == "2")
            {
                message = "Congratulations! You've won a new boat!";
            }
            else if (userValue == "3")
            {
                message = "Congratulations! You've won a new phone!";
            }
            else
            {
                message = "Sorry this input was not understood. You lose!";
            }

            Console.WriteLine(message);
            Console.ReadLine();
        }
    }
}
