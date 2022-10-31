import java.util.Arrays;

public class SortArray {
    public static void main(String[] args) {
        int[] array = new int[]{4,7,2,4,7,2,1,8,89,76};
        Arrays.sort(array);

        for (int i : array) {
            System.out.println(i);
        }
    }
}
