class Solution {

    public String encode(List<String> strs) {
        //Regular strings are immutable in java once a string object is created,
        //Stringbuilder uses a mutable character buffer internally instead of creating a new object whenever modifications are needed
        StringBuilder sb = new StringBuilder();

        for (String s : strs) {
            char[] c = s.toCharArray();
            int count = c.length;
            sb.append(count);
            sb.append('!');
            sb.append(s);
        }
        
        return sb.toString();
        
    }

    public List<String> decode(String str) {
        List<String> strs = new ArrayList(); //output arraylist of strings
        int i = 0;
        while (i < str.length()) {

            int j = i;
            //i to j is used to find the length of the string
            while (j < str.length() && str.charAt(j) != '!') {
                j++;
            }

            int length = Integer.parseInt(str.substring(i,j));
            j++; //move to after '!'

            String word = str.substring(j, j + length);
            strs.add(word); //add word to output arraylist
            i = j + length; //move i index to start of next word count start point
        }
        return strs;
    }
}
