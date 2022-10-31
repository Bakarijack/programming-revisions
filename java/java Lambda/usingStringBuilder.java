public class usingStringBuilder {
    public static void main(String[] args) {
        //using StringBuilder()
        StringBuilder stb = new StringBuilder();
        stb.append("Bakari");
        System.out.println(stb);

        //using StringBuilder(int capacity)
        StringBuilder stb1 = new StringBuilder(18);
        System.out.println("String capacity is = "+stb1.capacity());

        //using StringBuilder(CharSequence seq)
        StringBuilder stb2 = new StringBuilder("Kilu");
        System.out.println("The string is = "+stb2.toString());

        //using StringBuilder(String str)
        StringBuilder stb3 = new StringBuilder(stb);
        System.out.println("The string is = "+stb3.toString());

        //using insert 
        StringBuilder stb4 = new StringBuilder("Welcome");
        System.out.println(stb4.insert(3,"Java").toString());
    }
}
