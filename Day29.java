import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        while(t-->0){
            int n = in.nextInt();
            int k = in.nextInt();
            int max = 0;
            for(int i=1; i<=n; i++){
                for(int j=1+i; j<=n; j++){
                    int s = i & j;
                    if (s<k) max = Math.max(max, s);
                }
            }
            System.out.println(max);                       
        }
        in.close();
    }
}