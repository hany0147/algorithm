import java.util.*;


class Solution {
    public int solution(String s) {
        ArrayDeque<Character> stack = new ArrayDeque<>();
        
        for (char c : s.toCharArray()) {
            if (stack.isEmpty()) {
                stack.push(c);
            } else {
                char top = stack.peek();
                
                if (top == c) {
                    stack.pop();
                } else {
                    stack.push(c);
                }
            }     
        }
        
        return stack.isEmpty() == true ? 1 : 0;
    }
}