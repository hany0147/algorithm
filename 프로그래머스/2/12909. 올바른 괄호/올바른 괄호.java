import java.util.*;

class Solution {
    boolean solution(String s) {
        Stack<Character> stack = new Stack<>();

        for (char str : s.toCharArray()) {
            if (stack.isEmpty()) {
                if (str == ')') {
                    return false;
                }
                stack.push(str);
            } else {
                if (str == '(') {
                    stack.push(str);
                } else {
                    if (stack.pop() != '(') {
                        return false;
                    }
                }
            }
        }
        return stack.isEmpty();
    }
}