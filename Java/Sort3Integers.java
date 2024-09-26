public class Sort3Integers {
    public static void main(String[] args) {
        int x = Integer.parseInt(args[0]);
        int y = Integer.parseInt(args[1]);
        int z = Integer.parseInt(args[2]);
        //Your code here

        if (x > y && y > z) {
            System.out.printf("First = %d, Second = %d, Third = %d\n", x, y, z);
        }

        else if (x > z && z > y) {
            System.out.printf("First = %d, Second = %d, Third = %d\n", x, z, y);
        }

        else if (y > x && x > z) {
            System.out.printf("First = %d, Second = %d, Third = %d\n", y, x, z);
        }

        else if (y > z && z > x) {
            System.out.printf("First = %d, Second = %d, Third = %d\n", y, z, x);
        }

        else if (z > x && x > y) {
            System.out.printf("First = %d, Second = %d, Third = %d\n", z, x, y);
        }

        else if (z > y && y > x) {
            System.out.printf("First = %d, Second = %d, Third = %d\n", z, y, x);
        }
    }
}
