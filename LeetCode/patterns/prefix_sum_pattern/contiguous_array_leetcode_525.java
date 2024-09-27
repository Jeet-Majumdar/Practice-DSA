class Solution {
    public int findMaxLength(int[] nums) {
        if (nums.length == 0) return 0;
        Map<Integer, Integer> count_dict = new HashMap<>();
        int res = 0;
        int count = 0;

        count_dict.put(0, -1);
        
        for (int i = 0; i < nums.length; i++){
            int num = nums[i];
            if (num == 1) {
                count = count + 1;
            } else {
                count = count - 1;
            }

            if (!count_dict.containsKey(count)) {
                count_dict.put(count, i);
            } else {
                res = Math.max(res, i - count_dict.get(count));
            }
        }
        return res;
    }
}
