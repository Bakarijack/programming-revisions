public class TestStack {
    public static void main(String[] args) {
        Stack s = new Stack();

        s.push(10);
        s.push(20);
        s.push(100);

        System.out.println(s.pop()+" removed");
        System.out.println(s.peek()+" is the top now");
        s.print();
    }
}
