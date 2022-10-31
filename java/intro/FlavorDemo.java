public class FlavorDemo {
    static Demo d = new Demo(){       //Demo is the super class
        public void show(){
            super.show();
            System.out.println("Inside the flavorDemo class");
        }
    };

    public static void main(String[] args){
        d.show();
    }
}
