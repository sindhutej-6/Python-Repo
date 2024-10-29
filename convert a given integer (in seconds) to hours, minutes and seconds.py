import java.util.Scanner;
public class H{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int s = sc.nextInt();
        int h = s/3600;
        int r = s%3600;
        int m = r/60;
        int sec = r%60;
        System.out.println("H:M:S-"+h+":"+m+":"+sec);

    }
}