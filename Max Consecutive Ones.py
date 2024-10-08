import java.util.Scanner;
public class Maxcon{
    public  int MaXConOne(int[] num){
        int cn = 0;
        int maxone = 0;
        for(int i = 0;i<num.length;i++){
            if(num[i]==1){
                cn+=1;
            }
            else{
                maxone = Math.max(cn,maxone);
                cn = 0;
            }
        }
        return Math.max(maxone,cn);
    }
    public static void main(String args[]){
        Maxcon obj = new Maxcon();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int a[] = new int[n];
        for(int i = 0;i<n;i++){
            a[i]= sc.nextInt();
        }
        int c = obj.MaXConOne(a);
        System.out.println(c);

    }
}