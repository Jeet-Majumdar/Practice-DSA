class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double s = 0;
        for (int i = 0; i<k; i++){
            s = s + nums[i];
        }
        double avg = s / k;
        double max_avg = avg;
        for (int i = 1; i < (nums.length-k+1); i++){
            avg = (avg * k - nums[i-1] + nums[i+k-1]) / k;
            max_avg = Math.max(max_avg, avg);
        }
        return max_avg;
    }
}