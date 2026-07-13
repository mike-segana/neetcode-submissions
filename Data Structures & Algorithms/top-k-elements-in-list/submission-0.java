class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> count = new HashMap();
        //min heap to store (num, freq) pairs ordered by frequency
        PriorityQueue<Map.Entry<Integer, Integer>> minHeap = new PriorityQueue<>(Map.Entry.comparingByValue());
        int[] output = new int[k];
        for (int i: nums) {
            if (count.containsKey(i)) {
                count.put(i, count.get(i) + 1);
            } else {
                count.put(i, 1);
            }
        }
        //iterates through every num, freq pair in the map
        for (Map.Entry<Integer, Integer>entry : count.entrySet()) {
            //adds current num, freq pair to heap
            minHeap.offer(entry);

            if (minHeap.size() > k) {
                //if more than k elements, then smallest freq removed and only k most freq numbers remain
                minHeap.poll();
            }
        }
        
        //removes the k entries from the heap and stores their associated integer keys in the output array
        for (int i = 0; i < k; i++) {
            output[i] = minHeap.poll().getKey();
        }

        return output;
    }
}