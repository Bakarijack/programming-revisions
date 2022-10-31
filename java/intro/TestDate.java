import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class TestDate {
    public static void main(String[] args) {
        Date today = new Date();
        SimpleDateFormat formatter = new SimpleDateFormat("EEEE  MMMM dd, yyyy");

        System.out.println(formatter.format(today));

        Scanner input = new Scanner(System.in);
        System.out.print("Enter your three names : ");
        String names = input.next();
        names.trim();

        System.out.println("First name "+names.substring(0,names.indexOf(" ")+2));
        System.out.println();
        System.out.println();
        
    }
}
