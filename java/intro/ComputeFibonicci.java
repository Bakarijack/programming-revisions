import java.util.Scanner;

public class ComputeFibonicci {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the index for the fibonacci : ");
        int index = scanner.nextInt();

        System.out.println("The fibonacci of "+index+" is "+fib(index));
    }

    public static long fib(long index){
        if(index == 0){ 
         return 0;

        }else if(index == 1){  
         return 1;
        }else{  
         return fib(index - 1) + fib(index - 2);
        }
    }
}