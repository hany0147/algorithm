import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
    
        int[] first = {1, 2, 3, 4, 5};
        int[] second = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] third = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
         
        int first_score = 0;
        int second_score = 0;
        int third_score = 0;
        
        for (int i = 0; i < answers.length; i++) {
                if (first[i % first.length] == answers[i]) {
                    first_score += 1;
                }
            
               if (second[i % second.length] == answers[i]) {
                    second_score += 1;
                }
                if (third[i % third.length] == answers[i]) {
                    third_score += 1;
                }
        }
        
        ArrayList<Integer> arr = new ArrayList<>();
        int maxScore = Math.max(first_score, Math.max(second_score, third_score));
        
        if (first_score == maxScore) arr.add(1);
        if (second_score == maxScore) arr.add(2);
        if (third_score == maxScore) arr.add(3);
        
        return arr.stream().mapToInt(Integer::intValue).toArray();
    }
}