import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter first number: ");
        float first = scanner.nextFloat();

        System.out.print("Enter second number: ");
        float second = scanner.nextFloat();

        System.out.print("Enter operation (+, -, *, /): ");
        String operation = scanner.nextLine();

        switch (operation) {
            case "+":
                System.out.println("Result: " + (first + second));
                break;
            case "-":
                System.out.println("Result: " + (first - second));
                break;
            case "*":
                System.out.println("Result: " + (first * second));
                break;
            case "/":
                if (second != 0) {
                    System.out.println("Result: " + (first / second));
                } else {
                    System.out.println("Error: Division by zero!");
                }
                break;
            default:
                System.out.println("Unknown operation!");
                break;
        }

        scanner.close();
    }
}
