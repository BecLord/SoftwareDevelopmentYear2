package assignment2;

public class MergeSort {

    private static int[] merge(int[] A1, int[] A2)
    {
        // TASK 2.A.a
        //An array that will store the merged result
        int [] result = new int[A1.length + A2.length];
        int i = 0, j = 0, k = 0;

        //compare elements from both arrays and add the smaller one to the result array
        while (i < A1.length && j < A2.length) {
            if (A1[i] <= A2[j]) {
                result[k++] = A1[i++]; //add element from A1 to result and move pointer i
            }else {
                result[k++] = A2[j++]; //add element from A2 to result and move pointer j
            }
        }
        // if there are any remaining elements in A1, add them to the result
        while (i < A1.length) {
            result[k++] = A1[i++];
        }
        //if there are any remaining elements in A2, add them to the result
        while (j < A2.length) {
            result[k++] = A2[j++];
        }
        return result;
    }

    public static int[] mergesort(int[] A)
    {
        // TASK 2.A.b
        //if the array has 1 or 0 elements, it is already sorted
        if (A.length <= 1) {
            return A;
        }
        //find the middle index of the array
        int middle = A.length / 2;
        //create two arrays one for the left half and one for the right half
        int[] left = new int[middle];
        int[] right = new int[A.length - middle];

        //copy the left half of the array to the 'left'
        System.arraycopy(A, 0, left, 0, middle);

        //copy the right half of the array to the 'right'
        System.arraycopy(A, middle, right, 0, A.length - middle);

        //sort both halves
        left = mergesort(left);
        right = mergesort(right);

        //merge the two sorted halves and return
        return merge(left, right);
    }

    private static void print(int[] A)
    {
        for (int i=0; i<A.length; i++)
        {
            System.out.print(A[i] + ((i<A.length-1)?", ":""));
        }
        System.out.println();
    }

    public static void main(String[] args) {
        print(merge(new int[] {1,3,5,7,9}, new int[] {2,4,6,8}));
        print(mergesort(new int[] {5,2,8,1,3,9,7,4,6} ));
    }

}
