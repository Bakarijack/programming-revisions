public class TestClass {
    int radius;
    public static void main(String[] args) {
        TestClass obj1 = new TestClass();
        obj1.radius = 10;

        TestClass obj2 = obj1;

        System.out.println(obj1.radius);
        System.out.println(obj2.radius);
    }
}
