class Solution {
    public boolean isAnagram(String s, String t) {

        String sSorted = "";
        String tSorted = "";

        char[] sCharacters = s.toCharArray();
        char[] tCharacters = t.toCharArray();

        Arrays.sort(sCharacters);
        Arrays.sort(tCharacters);

        for(char character: sCharacters){
            sSorted = sSorted + character;
        }
        for(char character: tCharacters){
            tSorted = tSorted + character;
        }

        if(sSorted.equals(tSorted)){
            return true;
        }
        else{
            return false;
        }
    }
}
