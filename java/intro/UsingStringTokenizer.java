import java.util.StringTokenizer;

public class UsingStringTokenizer {
    public static void main(String[] args) {
        StringTokenizer st = new StringTokenizer("Bakari Mtua Kilu"," "); //split by the empty space. You can use , in pllace of " "

        while (st.hasMoreTokens()){
            System.out.println(st.nextToken());
        }
    }
}
