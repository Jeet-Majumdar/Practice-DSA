public class SelectionSort {
    public static void selectionSort(int[] arr) {
        int n = arr.length;

        // Loop through the array n-1 times
        for (int i = 0; i < n - 1; i++) {
            int minIndex = i;

            // Find the minimum element in the unsorted portion of the array
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }

            // Swap the minimum element with the first element of the unsorted portion
            int temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }
    }

    public static void main(String[] args) {
        int[] arr = {5, 3, 8, 4, 2};

        System.out.println("Before sorting:");
        for (int i : arr) {
            System.out.print(i + " ");
        }

        selectionSort(arr);

        System.out.println("\nAfter sorting:");
        for (int i : arr) {
            System.out.print(i + " ");
        }
    }
}
