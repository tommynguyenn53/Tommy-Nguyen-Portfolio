import java.lang.Math;

public class DieRoll {
    public static void main (String[] args) {

        int max = 6;
        int min = 0;
        int range = max - min + 1;

        int rand = (int) (Math.random() * range) + min;

        System.out.println(rand);
        }

    }

