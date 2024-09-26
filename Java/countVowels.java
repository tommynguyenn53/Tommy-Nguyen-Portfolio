public class countVowels {

    static int countVowels(String s) {
        int count = 0;
        char[] c = s.toCharArray(); // Convert the string to a character array
        char[] vowels = {'a', 'e', 'i', 'o', 'u'}; // Array of vowels

        // Loop through each character in the string
        for (char ch : c) {
            // Check if the character is a vowel
            for (char vowel : vowels) {
                if (ch == vowel) {
                    count++;
                    break; // No need to check other vowels if already matched
                }
            }
        }

        return count;
    }

    public static void main(String[] args) {
        String s = "astronaut";
        int count = countVowels(s);
        System.out.println("Number of vowels: " + count);
    }
}
