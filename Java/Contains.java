public class Contains {

    static boolean contains(int[] a, int element) {
        for (int i : a) {
            if (i == element)
                return true;

        }
        return false;
    }

    public static void main(String[] args) {
        int[] array = {1, 1, 5, 5, 5, 3, 8, 1};
        boolean result = contains(array, 5); //true
        System.out.print(result);
    }

}
