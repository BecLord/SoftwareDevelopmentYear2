package assignment1;

public class DoubleLinkedList implements List<Object> {
    private class ListNode {
        public ListNode(Object x) {
            key = x;
        }
        public Object key;
        public ListNode prev = null;
        public ListNode next = null;
    }

    private ListNode head;
    private ListNode tail;
    private int size;

    public DoubleLinkedList()
    {
        // TASK 1.A
        head = null;
        tail = null;
        size = 0;
    }

    public void prepend(Object x) {
        // TASK 1.B
        ListNode newNode = new ListNode(x);
        if (empty()) {
            head = newNode;
            tail = newNode;
        }else{
            newNode.next = head;
            head.prev = newNode;
            head = newNode;
        }
        size++;
    }

    public Object getFirst() {
        // TASK 1.C
        return head.key;
    }

    public void deleteFirst() {
        // TASK 1.D
        if (head == null){
           tail = null;
        }else{
            head.prev = null;
        }
        size--;
    }

    public void append(Object x) {
        // TASK 1.E
        ListNode newNode = new ListNode(x);
        tail.next = newNode;
        newNode.prev = tail;
        tail = newNode;
        size++;
    }

    public Object getLast() {
        // TASK 1.F
        return tail.key;
    }

    public void deleteLast() {
        // TASK 1.G
        tail.next = null;
        size--;
    }

    public boolean empty() {
        // TASK 1.H
        return size == 0;
    }

    public static void main(String[] args) {
        List<Object> test = new DoubleLinkedList();
        System.out.println(test.empty());
        for (int i=0; i<10; i++) {
            test.prepend(i + 100);
        }
        System.out.println(test.empty());
        for (int i=0; i<5; i++) {
            int x = (int)test.getFirst();
            System.out.print(x + " ");
            test.deleteFirst();
        }
        System.out.println();
        for (int i=0; i<10; i++) {
            test.append(i + 200);
        }
        while (!test.empty()) {
            int x = (int)test.getLast();
            System.out.print(x + " ");
            test.deleteLast();
        }
    }
}
