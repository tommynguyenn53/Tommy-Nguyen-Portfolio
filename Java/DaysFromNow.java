public class DaysFromNow {
    public enum Day {
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
        int y = Integer.parseInt(args[1]);

        int futureDayIndex = (x + y) % 7;

        System.out.println("The current day is " + Day.values()[x].name() + ", and in " + y + " days time it will be " + Day.values()[futureDayIndex].name());


    }
}
