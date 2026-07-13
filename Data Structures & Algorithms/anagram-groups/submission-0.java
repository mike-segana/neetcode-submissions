class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        //Map contains key and list index
        //If the sorted string s is in map then append s to list index
        //else add s to new sublist in output and add sorted string s to map with new sublist index
        List<List<String>> output = new ArrayList();
        HashMap<String, Integer> map = new HashMap();
        for (String s: strs) {
            char [] c = s.toCharArray();
            Arrays.sort(c);
            if (map.containsKey(String.valueOf(c))) {
                //append s to list at index retrieved from map
                output.get(map.get(String.valueOf(c))).add(s);
            } else {
                //add s to a new sublist in output
                //add sorted s to map with index of the sublist
                output.add(new ArrayList<>());
                output.get(output.size()-1).add(s);
                map.put(String.valueOf(c), output.size()-1);

            }
        }
        return output;
    }
}
