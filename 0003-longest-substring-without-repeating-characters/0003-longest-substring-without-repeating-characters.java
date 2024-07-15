class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> ss = new HashSet();
        int l = 0;
        int r = 0;
        int max = 0;
        while(r<s.length()){
            if(!(ss.contains(s.charAt(r)))){
                ss.add(s.charAt(r));
                max=Math.max(max, ss.size());
                r++;
            }
            else{
                ss.remove(s.charAt(l));
                l++;

            }
        }
        return max;
    }
}