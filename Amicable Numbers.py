import java.util.Scanner;
public class Amicable{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int as = 0, bs = 0;
        for(int i = 1;i<a;i++){
            if(a%i==0){
                as+=i;
            }
        }
        for(int i = 1;i<b;i++){
            if(b%i==0){
                bs+=i;
            }
        }
        if(a==bs && b==as){
            System.out.println("Amicable");
        }
        else{
            System.out.println("Not Amicable");
        }
    }
}