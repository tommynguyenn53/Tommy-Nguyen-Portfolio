public class Weekdays {

    public enum TimeOfDay {
        Sunday,
        Monday,
        Tuesday,
        Wednesday,
        Thursday,
        Friday,
        Saturday;
    }

    public static void main (String[] args) {
        int x = Integer.parseInt(args[0]);

        if (x == 0 || x == 6) {
            System.out.println("Day " + x + " of the week is: " + TimeOfDay.values()[x].name() + ". " + "It is a weekend.");

        }

        else {
            System.out.println("Day " + x + " of the week is: " + TimeOfDay.values()[x].name() + ". " + "It is not a weekend.");
        }


    }
}
