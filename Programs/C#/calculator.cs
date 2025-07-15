using System;

public class Project
{
    public static void Main(string[] args)
    {
	    Console.Write("Enter first number: ");
	    float first = Convert.ToSingle(Console.ReadLine());
	    Console.Write("Enter second number: ");
	    float second = Convert.ToSingle(Console.ReadLine());
	    Console.Write("Enter operation(+,-,*,/): ");
	    string operation = Console.ReadLine();
	    
	    if (operation == "+") {
	        float result = first + second;
	        Console.WriteLine("Result: " + Convert.ToString(result));
	    }
	    
	    else if (operation == "-") {
	        float result = first - second;
	        Console.WriteLine("Result: " + Convert.ToString(result));
	    }
	    
	    else if (operation == "*") {
	        float result = first * second;
	        Console.WriteLine("Result: " + Convert.ToString(result));
	    }
	    
	    else if (operation == "/") {
	        float result = first / second;
	        Console.WriteLine("Result: " + Convert.ToString(result));
	    }
	    
	    else {
	        Console.WriteLine("Unknown operation!");
	    }
    }
} 


