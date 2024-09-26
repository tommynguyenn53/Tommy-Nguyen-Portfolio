public class Count {

    static int count(int[] a, int element) {
        int count = 0;
        for (int i : a) {
            if (i == element)
                count ++;

        }
        return count;
    }

    public static void main(String[] args) {
        int[] array = {1, 1, 5, 5, 5, 3, 8, 1};
        int result = count(array, 3); //true
        System.out.print(result);
    }

}


