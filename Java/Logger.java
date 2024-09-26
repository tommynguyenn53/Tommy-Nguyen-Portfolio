import java.util.ArrayList;
import java.util.Scanner;

public class Logger {

    public static void main(String[] args) {

        ArrayList<String> list = new ArrayList<String>();

        Scanner scan = new Scanner(System.in);
        String input;


        while (!(input = scan.nextLine()).isEmpty()) {
            list.add(input);

        }
        for(String line: list) {
            System.out.println(line);
        }

    }
}