// https://www.acmicpc.net/problem/1085
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();
        int w = sc.nextInt();
        int h = sc.nextInt();

        int result = 0;

        result = Math.min(x,y);
        result = Math.min(result,Math.abs(x-w));
        result = Math.min(result,Math.abs(y-h));

        System.out.println(result);
    }
}