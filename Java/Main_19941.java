import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main_19941 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        StringTokenizer st = new StringTokenizer(line);
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        char[] arr = br.readLine().toCharArray();
        
        int res = 0;
        // System.out.println(n);
        // System.out.println(k);
        // System.out.println(Arrays.toString(arr));

        for(int i = 0; i < n; i++){

            boolean flag = false;

            if(arr[i] == 'P'){

                for(int j = i - k; j < i + k + 1; j ++) {

                    if(0 <= j && j < n && i != j && arr[j] == 'H'){

                        res++;
                        arr[j] = 'X';
                        // flag = true;
                        break;
                    }

                    // if(flag) {
                    //     break;
                    // }
                }
            }
        }

        System.out.println(res);
    

    }
}
