class Solution {
    public int[] productExceptSelf(int[] nums) {
        int count = 0;
        int total = 1;

        for (int i = 0; i < nums.length; i++) {
            count += 1;
        }

        //creating integer array with correct length initalises every element with value 1
        int[] output = new int[count];
        for (int i = 0; i < output.length; i++){
            output[i] = 1;
        }

        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < nums.length; j++) {
                if (i != j) {
                    output[i] = output[i] * nums[j];
                }
            }
        }
        return output;

    }
}  
