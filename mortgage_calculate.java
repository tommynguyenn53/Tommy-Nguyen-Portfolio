import java.text.NumberFormat;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Principal: ");
        int principal = scanner.nextInt();

        System.out.print("Annual Interest Rate (as a percentage): ");
        double annualRate = scanner.nextDouble();
        double monthlyRate = annualRate / 100 / 12;

        System.out.print("Period (in years): ");
        int years = scanner.nextInt();
        int months = years * 12;

        double mortgage = principal * (monthlyRate * Math.pow(1 + monthlyRate, months)) /
                (Math.pow(1 + monthlyRate, months) - 1);

        NumberFormat currencyFormat = NumberFormat.getCurrencyInstance();
        System.out.println("Monthly Mortgage Payment: " + currencyFormat.format(mortgage));
    }
}
