public class MethodInnerClass {
    public void outerMethod(){
        System.out.println("Outer class Method");
        int x = 4;   //not a good practise, make this final so that it can be accessed by the inner class methods

        //innerclass inside the out class's method
        class Inner{
            public void innerClassMethod(){
                System.out.println("Inside the inner class method");
                System.out.println(x);
            }
        }

        Inner in = new Inner();

        in.innerClassMethod();
    }
}
