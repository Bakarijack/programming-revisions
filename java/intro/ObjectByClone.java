public class ObjectByClone implements Cloneable {
    String name = "Bakari";

    @Override
    protected Object clone() throws CloneNotSupportedException{
        return super.clone();
    }
    public static void main(String[] args) {
        ObjectByClone obj1 = new ObjectByClone();

        try{
            ObjectByClone obj2 = (ObjectByClone) obj1.clone();
            System.out.println(obj2.name);
        }catch(CloneNotSupportedException e){
            e.printStackTrace();
        }
    }
}
