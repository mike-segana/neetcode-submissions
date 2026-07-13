class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        char[] s_characters = s.toCharArray();
        char[] t_characters = t.toCharArray();
        Arrays.sort(s_characters);
        Arrays.sort(t_characters);
        if (Arrays.equals(s_characters,t_characters)) {
            return true;
        }
        return false;
    }
}
