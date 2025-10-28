import java.util.Scanner;
import java.util.Random;
import java.util.Arrays;

public class SortDemo {

    // Bubble Sort
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        for (int j = n; j > 0; j--) {
            for (int i = 1; i < j; i++) {
                if (arr[i - 1] > arr[i]) {
                    int temp = arr[i - 1];
                    arr[i - 1] = arr[i];
                    arr[i] = temp;
                }
            }
        }
    }

    // Selection Sort
    public static void selectionSort(int[] arr) {
        int n = arr.length;
        for (int j = 0; j < n; j++) {
            int iMin = j;
            for (int i = j + 1; i < n; i++) {
                if (arr[i] < arr[iMin]) {
                    iMin = i;
                }
            }
            if (iMin != j) {
                int temp = arr[j];
                arr[j] = arr[iMin];
                arr[iMin] = temp;
            }
        }
    }

    // Generate random array
    public static int[] generateArray(int size) {
        Random rand = new Random();
        int[] arr = new int[size];
        for (int i = 0; i < size; i++) {
            arr[i] = rand.nextInt(10000); // Random number between 0 and 9999
        }
        return arr;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Bubble Sort Test
        System.out.println("🔹 Bubble Sort Test");
        System.out.print("Enter array size for Bubble Sort: ");
        int sizeBubble = scanner.nextInt();
        int[] bubbleArray = generateArray(sizeBubble);
        System.out.println("Original array: " + Arrays.toString(bubbleArray));
        bubbleSort(bubbleArray);
        System.out.println("Sorted array:   " + Arrays.toString(bubbleArray));

        // Selection Sort Test
        System.out.println("\n🔹 Selection Sort Test");
        System.out.print("Enter array size for Selection Sort: ");
        int sizeSelection = scanner.nextInt();
        int[] selectionArray = generateArray(sizeSelection);
        System.out.println("Original array: " + Arrays.toString(selectionArray));
        selectionSort(selectionArray);
        System.out.println("Sorted array:   " + Arrays.toString(selectionArray));

        scanner.close();
    }
}
