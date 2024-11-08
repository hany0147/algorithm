import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        Stack<Integer> stack = new Stack<>(); 
        int n = board.length;
        int[] reMoves = Arrays.stream(moves).map(m -> m - 1).toArray();
        
        for (int m : reMoves) {
            for (int i = 0; i < n; i++) {
                // 0이 아니면, 해당 숫자를 얻는다.
                int doll = board[i][m];
                
                if (doll != 0) {
                // 스택 통이 비어있지 않고, 안에 peek값고 해당 숫자가 같다면, answer += 2를 하고,
                // 스택 통을 pop한다.
                    if (!stack.isEmpty() && stack.peek() == doll) {
                        answer += 2;
                        stack.pop();
                    } else {
                        // 그렇지 않다면 해당 숫자를 push한다.
                        stack.push(doll);
                    }
                board[i][m] = 0;
                break;
                }
            }
        }
        
        return answer;
    }
}