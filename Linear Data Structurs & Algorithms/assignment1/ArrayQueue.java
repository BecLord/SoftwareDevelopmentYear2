package assignment1;

public class ArrayQueue implements Queue<Object> {
    private Object[] Q;
    private int frount;
    private int back;
    private int size;
    private int capacity;

    public ArrayQueue(int capacity) {
        // TASK 3.A.a
        this.capacity = capacity;
        Q = new Object[capacity];
        frount = 0;
        back = 0;
        size = 0;
    }

    public void enqueue(Object x) {
        // TASK 3.A.b
        Q[back] = x;
        size++;
    }

    public Object dequeue() {
        // TASK 3.A.c
        Object item = Q[frount];
        size--;
        return item;
    }

    public Object next() {
        // TASK 3.A.d
        return Q[frount];

    public boolean empty() {
        // TASK 3.A.e
        return size == 0;
    }

    public static void main(String[] args) {
        Queue<Object> test = new ArrayQueue(20);
        System.out.println(test.empty());
        for (int i=0; i<10; i++) {
            test.enqueue(i+100);
        }
        System.out.println(test.empty());
        System.out.println(test.next());
        for (int i=0; i<5; i++) {
            int x = (int)test.dequeue();
            System.out.print(x + " ");
        }
        System.out.println();
        for (int i=0; i<15; i++) {
            test.enqueue(i);
        }
        while (!test.empty()) {
            int x = (int)test.dequeue();
            System.out.print(x + " ");
        }
        System.out.println();
    }
}