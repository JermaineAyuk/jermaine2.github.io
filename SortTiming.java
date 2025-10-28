import java.util.Random;

public class SortTiming {

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
            arr[i] = rand.nextInt(10000);
        }
        return arr;
    }

    // Timing function
    public static double timeSort(String method, int size) {
        long totalTime = 0;
        for (int i = 0; i < 1000; i++) {
            int[] arr = generateArray(size);
            long start = System.nanoTime();

            if (method.equals("bubble")) {
                bubbleSort(arr);
            } else if (method.equals("selection")) {
                selectionSort(arr);
            }

            long end = System.nanoTime();
            totalTime += (end - start);
        }
        return totalTime / 1000.0 / 1_000_000.0; // Convert to milliseconds
    }

    public static void main(String[] args) {
        int[] sizes = {500, 2500, 5000};

        System.out.println("Timing Results (Average over 1000 runs):\n");

        for (int size : sizes) {
            double bubbleAvg = timeSort("bubble", size);
            double selectionAvg = timeSort("selection", size);

            System.out.printf("Array Size: %d\n", size);
            System.out.printf("Bubble Sort Avg Time: %.4f ms\n", bubbleAvg);
            System.out.printf("Selection Sort Avg Time: %.4f ms\n\n", selectionAvg);
        }
    }
}
