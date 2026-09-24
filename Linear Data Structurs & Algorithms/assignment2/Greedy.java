package assignment2;

import java.util.LinkedList;

public class Greedy {

    public static LinkedList<Activity> activitySelection(LinkedList<Activity> activities) {
        // TASK 1.B.a
        //create a list to store selected activities
        LinkedList<Activity> selectedActivities = new LinkedList<>();

        //pick the first activity
        Activity lastSelected = activities.getFirst();
        selectedActivities.add(lastSelected);

        //go through the activities and select the ones that don't overlap
        for (int i = 1; i < activities.size(); i++) {
            Activity current = activities.get(i);

            //if the activity doesn't overlap with the last selected one, pick it
            if (!lastSelected.overlap(current)) {
                selectedActivities.add(current);
                lastSelected = current;
            }
        }
        return selectedActivities; //return the list of selected activities
    }

    public static LinkedList<Integer> makeChange(int amount, int[] denominations) {
        // TASK 1.B.b
        //create a list to store the change
        LinkedList<Integer> change = new LinkedList<>();

        //loop through the denominations and subtract from the amount
        for (int i = 0; i < denominations.length; i++) {
            //add denomination until the amount is less than the denomination
            while (amount >= denominations[i]) {
                change.add(denominations[i]);
                amount -= denominations[i]; //subtract denomination from amount
            }
            //if the amount is 0, stop
            if (amount == 0) {
                break;
            }
        }
        return change; // return the list of change
    }

    public static void main(String[] args) {
        LinkedList<Activity> activities = new LinkedList<Activity>();
        activities.add(new Activity(1,1, 4));
        activities.add(new Activity(2, 3, 5));
        activities.add(new Activity(3, 0, 6));
        activities.add(new Activity(4, 5, 7));
        activities.add(new Activity(5, 3, 8));
        activities.add(new Activity(6, 5, 9));
        activities.add(new Activity(7, 6, 10));
        activities.add(new Activity(8, 8, 11));
        activities.add(new Activity(9, 8, 12));
        activities.add(new Activity(10, 2, 13));
        activities.add(new Activity(11, 12, 14));
        activitySelection(activities).forEach(a -> a.print());

        System.out.println();
        makeChange(1234, new int[] { 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1 }).forEach(i -> System.out.println(i));
    }
}
