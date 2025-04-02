import java.util.Scanner;

public class Main {
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String str = sc.next();

        // 보너스 값 초기화
        int bouns = 0;
        int result = 0;

        for(int i = 0; i < n; i++){
            if(str.charAt(i) == 'O'){
                result = result + (i+1) + bouns;
                bouns++;
            } else{
                bouns = 0;
            }
        }
        System.out.println(result);
    }
}