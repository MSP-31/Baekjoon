import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();


        int[] arr = new int[n];

        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }

        System.out.println(sum(arr, m));
    }

    public static int sum(int[] arr, int m){
        int sum, result = 0;

        for(int i = 0; i < arr.length-2; i++){
            for(int j = i+1; j < arr.length; j++){
                for(int k = j+1; k < arr.length; k++){
                    sum = arr[i] + arr[j] + arr[k];
                    if (sum == m){
                        return sum;
                    }else if (sum <= m){
                        result = Math.max(result, sum);
                    }
                }
            }
        }
        return result;
    }
}