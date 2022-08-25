using System;

namespace Variables
{
    class Program
    {
        static void Main(string[] args)
        {
            // Declaring integer variables and adding them together.
            /*
            int x;
            int y;

            x = 7;
            y = x + 8;

            Console.WriteLine(y);
            */

            // Declaring string and implicit type variable 'var' (specifies the type
            // of a variable based on initial value) and concatenating them together.
            /*
            string myFirstName = "Thomas";
            var myLastName = "Croos";

            Console.WriteLine(myFirstName + ' ' + myLastName);
            Console.ReadLine();
            */

            // Dealing with different variable types and applying variable type conversions
            // depending on the initial type of variable declared.
            int x = 7;
            //string y = "Alex";
            string y = "5";
            string myFirstTry = x.ToString() + y;

            int mySecondTry = x + int.Parse(y);

            Console.WriteLine(myFirstTry);
            Console.WriteLine(mySecondTry);
            Console.ReadLine();

        }
    }
}
