public class GFG {
    static Hello h = new Hello(){

        @Override
        public void show() {
            // TODO Auto-generated method stub
            System.out.println("Implemented method");
        }

    };

    public static void main(String[] args) {
        h.show();
    }
}
