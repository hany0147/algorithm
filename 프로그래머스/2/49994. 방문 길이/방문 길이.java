import java.util.*;

class Solution {
    public int solution(String dirs) {
        int answer = 0;
        
        // 방향 초기화
        
        HashMap<String, int[]> dirMap = new HashMap<>();
        dirMap.put("U", new int[]{1, 0});
        dirMap.put("D", new int[]{-1, 0});        
        dirMap.put("R", new int[]{0, 1});
        dirMap.put("L", new int[]{0, -1});
        
        // 변수 초기화
        HashSet<String> set = new HashSet<>();
        
        int[] init = new int[2];
        
        for (char dir : dirs.toCharArray()) {
            int x = dirMap.get(String.valueOf(dir))[0];
            int y = dirMap.get(String.valueOf(dir))[1];
            
            int newX = x + init[0];
            int newY = y + init[1];
            
            if (newX < -5 || newX > 5 || newY < -5 || newY > 5) {
                continue;
            }
            

            // 양방향 경로를 고려해 저장
            String path1 = init[0] + "," + init[1] + "," + newX + "," + newY;
            String path2 = newX + "," + newY + "," + init[0] + "," + init[1];
            set.add(path1);  // 첫 경로 추가
            set.add(path2);  // 역방향 경로 추가
            
            init[0] = newX;
            init[1] = newY;
        }
        
        
        return set.size() / 2;
    }
}