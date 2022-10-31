import java.util.Scanner;

public class CheckInput {
    public static void main(String[] args) {
        boolean flag = false;
        Scanner scanner = new Scanner(System.in);


        do{
            try{
                System.out.print("Enter an interger : ");
                int num = scanner.nextInt();

                while(num==0){
                    System.out.println("number cannot be zero");
                    System.out.print("Enter an interger : ");
                    num = scanner.nextInt();
                }

                System.out.println("Input is "+num);
                flag = true;
            }catch(Exception e){
                System.out.println("Wringo input!");
                scanner.nextLine();
            }
        }while(!flag);
    }
}
