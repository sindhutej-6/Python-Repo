import java.util.Scanner;
public class Day{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int d = sc.nextInt();
        int y = d/365;
        int z = d%365;
        int da = z/7;
        System.out.println(y);
        System.out.println(da);
    }
}