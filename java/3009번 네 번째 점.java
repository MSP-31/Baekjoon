import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        /* 해시맵을 이용한 풀이 */
        /*
        HashMap<Integer, Integer> mapa = new HashMap<>();
        HashMap<Integer, Integer> mapab = new HashMap<>();

        Scanner sc = new Scanner(System.in);
        int a ,b;

        for (int i = 0; i < 3; i++) {
            a = sc.nextInt();
            b = sc.nextInt();

            if(mapa.containsKey(a)) mapa.put(a, mapa.get(a) + 1);
            else mapa.put(a, 1);

            if(mapab.containsKey(b)) mapab.put(b, mapab.get(b) + 1);
            else mapab.put(b, 1);
        }

        for (Map.Entry<Integer, Integer> entry : mapa.entrySet()) {
            if(entry.getValue() == 1) System.out.print(entry.getKey() + " ");
        }
        for (Map.Entry<Integer, Integer> entry : mapab.entrySet()) {
            if(entry.getValue() == 1) System.out.print(entry.getKey());
        }
         */

        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        int c = sc.nextInt();
        int d = sc.nextInt();

        int ra = sc.nextInt();
        int rb = sc.nextInt();

        if (a != c){
            if (a == ra) ra = c;
            else if (c == ra) ra = a;
        }
        if (b != d){
            if (b == rb) rb = d;
            else if (d == rb) rb = b;
        }

        System.out.printf("%d %d", ra, rb);
    }
}