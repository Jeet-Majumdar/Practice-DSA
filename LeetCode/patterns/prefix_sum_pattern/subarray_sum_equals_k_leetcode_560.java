import java.util.HashMap;
import java.util.Map;

class Solution {
    public int subarraySum(int[] nums, int k) {
        if (nums.length == 0) return 0;
        Map<Integer, Integer> prefix_dict = new HashMap<>();
        
        prefix_dict.put(0, 1);
        int prefix_sum = 0;
        int res = 0;

        for (int i =0; i < nums.length; i++){
            prefix_sum += nums[i];
            
            if ( prefix_dict.containsKey(prefix_sum - k)){
                res += prefix_dict.get(prefix_sum - k);
            }
            int val = prefix_dict.getOrDefault(prefix_sum, 0) + 1;
            prefix_dict.put(prefix_sum, val); 
        }
    
    return res;

    }
}