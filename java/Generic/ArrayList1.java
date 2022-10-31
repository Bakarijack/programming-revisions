import java.util.ArrayList;
import java.util.Date;

public class ArrayList1 {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();    //generic ArrayList
        list.add(68);
        list.add(56);
        list.add(77);

        for(int number : list){          //java foreach loop
            System.out.println(number);
        }

        Date date1 = new Date(1000);
        Comparable<Date> c = new Date();
        System.out.println(c.compareTo(date1));

        ArrayList<Character> charList = new ArrayList<>();
        charList.add('a');
        charList.add('b');
        charList.add('c');

        for(char  latter : charList){
            System.out.println(latter);
        }

        ArrayList test = new ArrayList();
        test.add(new Date());
        Date date =(Date) test.get(0);    //need to cast in the normal using of ArrayList
    }
}
