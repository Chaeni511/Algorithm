package Java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;
import java.util.StringTokenizer;

/**
 * Main_1932
 */
public class Main_prac {
    public static void main(String[] args) throws Exception {
        // 입력 받는 첫번째 방법 Scanner
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 5
        // 5 10 15 20 7

        // String testCaseStr = br.readLine();
        // int tc = Integer.parseInt(testCaseStr);
        
        int tc = Integer.parseInt(br.readLine());

        String line = br.readLine();
        StringTokenizer st = new StringTokenizer(line);
        int[] arr = new int[tc];
        for(int i = 0; i < tc; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            System.out.println(i);
            System.out.println(arr[i]);
        }

        List<Integer> list = new ArrayList<>();
        List<Integer> linkedList = new LinkedList<>();
        Queue<Integer> que = new LinkedList<>();
        LinkedList<Integer> linked = new LinkedList<>();
        

        System.out.println(Arrays.toString(arr));
        

    }
}