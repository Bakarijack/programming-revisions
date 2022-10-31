import java.io.IOException;

public class GetChar {
    public static void main(String[] args) throws IOException {
        char ch;

        System.out.print("Enter any input: ");
        ch = (char) System.in.read();  //return int hence must be cast int char

        //output the char entered
        System.out.println(ch);
    }
}
