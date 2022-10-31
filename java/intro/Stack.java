public class Stack {
    final static  int MAX_SIZE = 1000;
    int top;
    int a[] = new int[MAX_SIZE];

    Stack(){
        top = -1;
    }

    public boolean isEmpty() {
        return (top < 0);
    } 
    public boolean push(int x){   
        if(top > (MAX_SIZE -1) ){
            System.out.println("Stack overflow");
            return false;
        }else{
            a[++top] = x;
            System.out.println("Pushed successfuly");
            return true;
        }
    }

    public int  pop(){
        if(top < 0){
            System.out.println("Stack Underflow");
            return 0;
        }else{
            int x = a[top--];
            return x;
        }
    }

    public int peek(){
        if(top < 0){
            System.out.println("Stack Underflow");
            return 0;
        }else{
            int x = a[top];
            return x;
        }
    }

    public void print(){
        for (int i = top; i > -1; i--){
            System.out.println(" "+a[i]);
        }
    }

}
