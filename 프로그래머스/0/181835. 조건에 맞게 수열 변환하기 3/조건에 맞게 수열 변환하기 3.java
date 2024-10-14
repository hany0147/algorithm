class Solution {
   
    public int[] solution(int[] arr, int k) {
        int size = arr.length;
        int[] answer = new int[size];
        
        if (k % 2 == 0) {
            return work(arr,size, k, false);
        }
        else {
            return work(arr, size, k, true);
        }
        
    }
    
    private int[] work(int[] arr, int size, int k, boolean isOdd) {
        if (isOdd) {
            for (int i = 0; i < size; i++) {
                arr[i] *= k;
            }
        } else {
            for (int i = 0; i < size; i++) {
                arr[i] += k;
            }
        }
        return arr;
    }
}