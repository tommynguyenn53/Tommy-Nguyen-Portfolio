import java.util.Scanner;

public class Grade {
    public static void main(String[] args) {

        System.out.print("What mark did you receive for this unit? ");
        Scanner scan = new Scanner(System.in);

        int grade = scan.nextInt();

        if (grade >= 85) {
            System.out.println("You received a High Distinction");
        }

        else if (grade >= 75) {
            System.out.println("You received a Distinction");

        }

        else if (grade >= 65) {
            System.out.println("You received a Credit");
        }

        else if (grade >= 50) {
            System.out.println("You received a Pass");
        }

        else {
            System.out.println("You received a Fail");
        }



    }
}
