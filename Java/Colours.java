import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Colours {
    public static void main(String[] args) {

        Map<String, String> colours = new HashMap<>();

        Scanner scanner = new Scanner(System.in);



        while (true) {
            System.out.println("Input a colour along with its RGB code: ");
            String code = scanner.nextLine();



            if (code.isEmpty()) {
                System.out.println(colours);
                break;
            }
            String[] input = code.split("->");


            String colourName = input[0];
            String rgbstring = input[1];

            colours.put(colourName, rgbstring);

            System.out.println(colours + "\n");



        }

        scanner.close();
    }
}
