public class MainC extends Product {

    @Override
    public int product(int num1, int num2) {
        // TODO Auto-generated method stub
        return num1 *num2;
    }

    public static void main(String[] args) {
        MainC obj = new MainC();

        int pro = obj.product(3, 4);
        System.out.println(pro);
    }
    
}
