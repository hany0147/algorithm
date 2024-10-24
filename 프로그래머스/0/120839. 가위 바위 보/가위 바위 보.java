import java.util.HashMap;

class Solution {
    public String solution(String rsp) {
        StringBuilder answer = new StringBuilder();
        HashMap<String, String> win = new HashMap<>();
        win.put("2", "0");
        win.put("0", "5");
        win.put("5", "2");
        
        for (int i = 0; i < rsp.length(); i++) {
            answer.append(win.get(String.valueOf(rsp.charAt(i)))); 
        }
        return answer.toString();
    }
}