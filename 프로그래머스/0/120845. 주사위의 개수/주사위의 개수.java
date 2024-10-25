class Solution {
    public int solution(int[] box, int n) {
        int total = box[0] * box[1] * box[2];
        int answer = (box[0] / n) * (box[1] / n) * (box[2] / n);
        return answer;
    }
}