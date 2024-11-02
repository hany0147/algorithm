import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        
        for (int i = 0; i < s.length(); i++) {
            if (isCorrect(s)) {
                answer++;
            }
            
            s = s.substring(1) + s.charAt(0);
        }
        
        return answer;
    }
    
    private boolean isCorrect(String s) {
        ArrayDeque<Character> stack = new ArrayDeque<>();
        
        for (char c : s.toCharArray()) {
        
            if (c == '[' || c == '{' || c == '(') {
                stack.push(c);                    
            } else {
                if (stack.isEmpty()) {
                    return false;
                }
                char top = stack.pop();
                
                if ((c == ']' && top != '[') ||
                    (c == '}' && top != '{') ||
                    (c == ')' && top != '(')) {
                    return false;
                }
            }
        }
        
        return stack.isEmpty();
    }
}