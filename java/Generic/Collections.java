import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Collections {
    public static void main(String[] args) {
        List<String> fruits = new ArrayList<>();
        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Strawbery");

        System.out.println("loop 1");
        for (int i=0; i < fruits.size();i++){
            System.out.println(fruits.get(i));
            if("Apple".equals(fruits.get(i))){
                fruits.remove(i);
            }
        }

        System.out.println("loop 2");
        for (String fruit : fruits) {
            System.out.println(fruit);
            if("Apple".equals(fruit)){
                fruits.remove(fruit);
            }
        }

        System.out.println("Loop 3");
        Iterator<String> fruitIterator = fruits.iterator();
        while(fruitIterator.hasNext()){
            String fruit = fruitIterator.next();
            System.out.println(fruit);
            if("Apple".equals(fruit)){
                fruitIterator.remove();
                System.out.println(fruitIterator.next());
            }
        }
    }
}
