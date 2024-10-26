import java.util.List;
import java.util.ArrayList;

class Solution {
    public List solution(int n) {
        List<Integer> answer = new ArrayList<>();
        for (int i = 1; i < n + 1; i++) {
            if (n % i == 0) {
                answer.add(i);
            }
        }
        return answer;
    }
}