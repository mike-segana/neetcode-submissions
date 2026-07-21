class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> values = new HashSet<Integer>();
        int longest_seq = 0;
        //Arrays.sort(nums); - cant use because longer than O(n)
        for (int i : nums) {
            if (values.contains(i) == false) {
                values.add(i);
            }
        }
        for (int i : nums) {
            if (values.contains(i-1) == false) {
                int seq_count = 1;
                int current_int = i; //set i as start point because nothing is before it

                while (values.contains(current_int + 1)) {
                    //while there is an int after current int i in hashset increment to next int and increment counter
                    current_int++;
                    seq_count++;
                }
                if (longest_seq < seq_count) {
                    longest_seq = seq_count;
                }
            }
            
        }
        
        return longest_seq;
    }
}
