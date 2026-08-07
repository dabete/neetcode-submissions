class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> dict = new HashMap<>();
        for(int number: nums){
            if(dict.containsKey(number)==false){
                dict.put(number, 1);
            }
            else{
                return true;
            }
        }
        return false;
    }
}