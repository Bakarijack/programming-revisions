import java.text.DecimalFormat;

public class SquareRoot {
    public static void main(String[] args) {
        System.out.printf("%.2f",Math.sqrt(32));
        System.out.println();
        if(10>9) System.out.println("Execute this statement");

        //format a number
        DecimalFormat formater = new DecimalFormat("#,###.00");
        double x = 1234567.5768;
        System.out.println(formater.format(x));
    }
}
