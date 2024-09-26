import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;


public class CharacterOccurrence {
    public static void main(String[] args) {
        Map<Character, Integer> map = new HashMap<>();

        System.out.print("Input a string: ");

        Scanner scanner = new Scanner(System.in);

        String input = scanner.nextLine();
        char[] c = input.toCharArray();

        for (int i = 0; i < input.length(); i++) {
            if (map.containsKey(c[i])) {
                map.put(c[i], map.get(c[i]) + 1);
            }
            else {
                map.put(c[i], 1);
            }
        }

        System.out.println(map);

    }
}
