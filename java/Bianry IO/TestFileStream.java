import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class TestFileStream {
    public static void main(String[] args)  throws IOException{
        try (
            FileOutputStream output = new FileOutputStream("/home/root123/temp.dat");  //save the file in a specified directory
        ){
            for (int i = 0;i <= 10; i++){
                output.write(i);
            }
        }

        //creating an input stream for the file
        try(
            FileInputStream input = new FileInputStream("temp.dat");
        ){
            int value;
            while ((value = input.read()) != -1){
                System.out.println(value+" ");
            }
        }
    }
}
