package assignment2;

public class DivideAndConquer {

    public static int fibonacci(int n) {
        // TASK 1.A.a
        if (n == 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        }else {
            return fibonacci(n - 1) + fibonacci(n - 2);
        }
    }

    public static int search(int[] A, int v)
    {
        // TASK 1.A.b
        int low = 0; //start of the array
        int high = A.length - 1; //end of the array

        while (low <= high) {
            //find the middle index of the array
            int middle = (low + high) / 2;

            if (A[middle] == v) {
                return middle; //if the middle element is the value we are looking for, return
            } else if (A[middle] > v) {
                high = middle - 1; //if the middle element is greater than the value, search the left half
            }else {
                low = middle + 1; //if the middle element is less than the value, search the right half
            }
        }
        return -1;
    }

    public static void hanoi(int n, char A, char B, char C)
    {
        // TASK 1.A.c
        //if only one disk is left, move it directly from A to C
        if (n == 1) {
            System.out.println(A + "->" + C);
            return;
        }

        // move n-1 disks from A to B using C as a temporary stop
        hanoi(n - 1, A, C, B);
        //move the nth disk from A to C
        System.out.println(A + "->" + C);
        //move the n-1 disks from B to C, suing A as a temporary stop
        hanoi(n - 1, B, A, C);
    }

    public static void main(String[] args) {
        for (int i=0; i<10; i++) {
            System.out.println(fibonacci(i));
        }
        System.out.println();
        for (int i=0; i<10; i++) {
            System.out.println(search(new int[]{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, i));
        }
        System.out.println();
        hanoi(4, 'A', 'B', 'C');
    }
}
