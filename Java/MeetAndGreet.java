import java.util.Scanner;

public class MeetAndGreet {
    public static void main(String[] args) {

        System.out.printf("Hi, What's your name? ");

        Scanner scanner = new Scanner(System.in);

        String name = scanner.nextLine();

        System.out.println("Hello " + name + "!");
    }
}
