import java.util.Arrays;

public class GenericMethodDemo {
    public static void main(String[] args) {
        Integer[] integers = {1,3,2,5,4};
        String[] names = {"Bakari","Mtua","Kilu"};

        Arrays.sort(names);
        Arrays.sort(integers);
        GenericMethodDemo.<Integer>print(integers);
        GenericMethodDemo.<String>print(names);
        print(names);
    }

    public static <E> void print(E[] list){
        for(E element : list){
            System.out.print(element+" ");
        }       
        System.out.println();
    }
}
