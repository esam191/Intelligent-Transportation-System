
public class Main{

public static void main(String[] args) {
    
    System.out.println("Hello World");
    int count = 0;
    while(true){
        try {
            Thread.sleep(2*1000);
            System.out.println("I am still here Iteration " + count++);
        } catch (InterruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

    }
}
}