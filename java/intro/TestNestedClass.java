public class TestNestedClass {
    public static void main(String[] args){
        Outer.Inner inObj = new Outer().new Inner();  //creating object for the inner class
        inObj.show();
    }
}
