class NumArray {
    int[] arr;
    public NumArray(int[] nums) {
        this.arr = nums;
    }
    
    public int sumRange(int left, int right) {
        int res = 0;
        for (int i = left; i <= right; i++){
            res = this.arr[i] + res;
        }
        return res;
    }
}