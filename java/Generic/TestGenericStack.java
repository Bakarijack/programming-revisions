public class TestGenericStack {
    public static void main(String[] args) {
        GenericStack<String>  city = new GenericStack<>();
        city.push("Mombasa");
        city.push("Nairobi");
        city.push("Kisumu");

        GenericStack<Integer> numbers = new GenericStack<>();
        numbers.push(1);
        numbers.push(14);
        numbers.push(10);

        System.out.println(numbers.toString());
        System.out.println(city.toString());
        System.out.println(numbers.pop());
        System.out.println(numbers.toString());
    }
}
