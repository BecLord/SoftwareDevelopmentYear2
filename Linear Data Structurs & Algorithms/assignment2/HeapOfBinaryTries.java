package assignment2;

public class HeapOfBinaryTries {
    private BinaryTrie[] A;
    private int heapsize;

    private void heapify(int i)
    {
        // TASK 3.A.a
        int left = 2 * i + 1; //left child index
        int right = 2 * i + 2; //right child index

        int smallest = i;

        //check if the left child is smaller than the current node
        if (left < heapsize && A[left].compare(A[smallest])) {
            smallest = left;
        }

        //check if the right child is smaller than the current node
        if (right < heapsize && A[right].compare(A[smallest])) {
            smallest = right;
        }

        //if the smallest is not the current node, swap and continue to heapify
        if (smallest != i) {
            BinaryTrie temp = A[i];
            A[i] = A[smallest];
            A[smallest] = temp;

            heapify(smallest);
        }
    }

    public HeapOfBinaryTries(BinaryTrie[] A)
    {
        // TASK 3.A.b
        this.A = A;
        this.heapsize = A.length;

        for (int i = heapsize / 2 - 1; i >= 0; i--) {
            heapify(i);
        }
    }

    public BinaryTrie extractMin()
    {
        // TASK 3.A.c
        if (heapsize == 0) {
            throw new IllegalStateException("The Heap is empty");
        }

        BinaryTrie min = A[0]; //the root is the minimum
        A[0] = A[heapsize - 1]; //move the last element to the root
        heapsize--; //decrease the heap size

        heapify(0); //restore the heap property

        return min;
    }

    public void insert(BinaryTrie x) {
        // TASK 3.A.d
        if (heapsize == A.length) {
            throw new IllegalStateException("The Heap is full");
        }

        A[heapsize] = x; //add the new element to the heap
        heapsize++;

        //move the new element to its correct position in the heap
        int i = heapsize - 1;

        while (i > 0 && A[(i - 1) / 2].compare(A[i])) {
            BinaryTrie temp = A[i];
            A[i] = A[(i - 1) / 2];
            A[(i - 1) / 2] = temp;

            i = (i - 1) / 2; //move up to the parent
        }
    }

    public int size()
    {
        return heapsize;
    }
}
