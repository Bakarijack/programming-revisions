public class StaticNestedClass {
    public static void outerMethod() {
     System.out.println("Inside the outer method");   
    }

    static class Inner{
        public static void display(){
            System.out.println("Inside inner class method");
            outerMethod();
        }
    }
}
