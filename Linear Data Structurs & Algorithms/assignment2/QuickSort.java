package assignment2;

public class QuickSort {

    private static int partition(int[] A, int p, int r)
    {
        // TASK 2.B.a
        int pivot = A[r];
        int i = p - 1;

        //loop through the array and move elements smaller than pivot to the left
        for (int j = p; j < r; j++) {
            //if the current element is smaller or equal to the pivot, move i to the right
            if (A[j] <= pivot) {
                i++;
                //swap the current element with the element at position i
                int temp = A[i];
                A[i] = A[j];
                A[j] = temp;
            }
        }
        //put the pivot in its correct place by swapping it with A[i +1]
        int temp = A[i + 1];
        A[i + 1] = A[r];
        A[r] = temp;

        return  i + 1;
    }

    private static void quicksort(int[] A, int p, int r)
    {
        // TASK 2.B.b
        if (p < r) {
            //divide the array into two parts by finding pivots index
            int pivotIndex = partition(A, p, r);

            quicksort(A, p, pivotIndex - 1); //sort the left part of the array
            quicksort(A, pivotIndex + 1, r); //sort the right part of the array
        }

    }

    public static void quicksort(int[] A)
    {
        quicksort(A, 0, A.length-1);
    }

    private static void print(int[] A)
    {
        for (int i = 0; i < A.length; i++)
        {
            System.out.print(A[i] + ((i < A.length - 1) ? ", " : ""));
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int[] A = new int[] {5,2,8,1,3,9,7,4,6};
        quicksort(A);
        print(A);
    }

}
