import java.util.*;

class Solution {
    public int[] solution(int N, int[] stages) {
        HashMap<Integer, Double> map = new HashMap<>();
        for (int i = 1; i <= N; i++) {
            double failureRate = 0;
            double child = 0;
            double parent = 0;
            for (int stage : stages) {
                if (stage >= i) {
                    parent += 1;
                }
                if (stage == i) {
                    child += 1;
                }
            }
            failureRate = (parent == 0) ? 0 : (child / parent); // parent가 0일 경우 failureRate를 0으로 설정
            map.put(i, failureRate);
        }
        
        // Stream을 이용하여 실패율 내림차순, 스테이지 번호 오름차순으로 정렬 후 배열로 변환
        return map.entrySet().stream()
            .sorted((e1, e2) -> {
                int cmp = e2.getValue().compareTo(e1.getValue());
                return (cmp != 0) ? cmp : e1.getKey().compareTo(e2.getKey());
            })
            .mapToInt(Map.Entry::getKey)
            .toArray();
    }
}
