import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Shopping {
    String item;
    int quantity;

    public Shopping(String item, int quantity) {
        this.item = item;
        this.quantity = quantity;
    }
    public String getItem() {
        return item;
    }

    public void setItem(String item) {
        this.item = item;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public static void main (String[] args) throws FileNotFoundException {
        File f = new File("src/shopping.txt");
        Scanner scan = new Scanner(f);
        while(scan.hasNextLine()) {
            String s = scan.nextLine();
            String[] data = s.split(":");
            String item = data[0];
            int quantity = Integer.parseInt(data[1]);

            Shopping shopping = new Shopping(item, quantity);
            System.out.println("Item: " + shopping.item + ", " + "quantity: "+ shopping.quantity);
        }



    }




}
