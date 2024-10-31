class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {

        int arr1Size = arr1.length;
        int arr2Size = arr2.length;
        int arr2InnerSize = arr2[0].length;
        int[][] answer = new int[arr1Size][arr2InnerSize];
        for (int i = 0; i < arr1Size; i++) {
            for (int j = 0; j < arr2InnerSize; j++) {
                int tmp = 0;
                for (int k = 0; k < arr1[i].length; k++) {
                    tmp += (arr1[i][k] * arr2[k][j]);
                }
                answer[i][j] = tmp;
            }
        }
        return answer;
    }
}