import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class RollCall {
    public static void main(String[] args) {

        Map<String, Integer> petCount = new HashMap<>();

        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.print("Please sign in/out your pet: ");
            String input = scanner.nextLine();

            if (input.isEmpty()) {
                break;
            }

            String[] details = input.split(" ");

            if (details.length != 3) {
                System.out.println("Invalid input");
                continue;
            }

            String action = details[0];
            String petType = details[1];
            String petName = details[2];

            if (action.equals("In")) {
                petCount.put(petType, petCount.getOrDefault(petType, 0) + 1);
            }

            else if (action.equals("Out")) {
                if (petCount.containsKey(petType) && petCount.get(petType) > 0) {
                    petCount.put(petType, petCount.getOrDefault(petType, 0) - 1);
                } else {
                    System.out.println("No " + petType + " to check out.");
                }

            } else {
                System.out.println("Invalid action: " + action);
                continue;
            }

            for (Map.Entry<String, Integer> entry : petCount.entrySet()) {
                System.out.println(entry.getKey() + " " + entry.getValue());
            }


        }
    }
}
