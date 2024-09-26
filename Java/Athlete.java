import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Athlete {
    String name;
    double time;

    public Athlete(String name, double time) {
        this.name = name;
        this.time = time;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getTime() {
        return time;
    }

    public void setTime(double time) {
        this.time = time;
    }

    public static void main (String[] args) throws FileNotFoundException {
        File f = new File("src/athlete.txt");
        Scanner scan = new Scanner(f);
        while(scan.hasNextLine()) {
            String s = scan.nextLine();
            String[] data = s.split(",");
            String name = data[0];
            double time = Double.parseDouble(data[1]);

            Athlete athlete = new Athlete(name, time);
            System.out.println("Name: " + athlete.name + ", " + "time: "+ athlete.time);
        }



    }
}
