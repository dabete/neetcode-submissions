class Solution {
public:

void backtrack(int sum, vector<int> &numbers, int index, int target, vector<vector<int>> &result, vector<int> &nums) {
            // base case - current number is more than target
            // we probably also need a base case using the index, e.g. if longer than the size of the array 
            if (index >= nums.size()){
                return;
            } 
            if(sum > target){
                return;
            }

            if(sum == target) {
                result.push_back(numbers);
                return;
            }

           // include 
           numbers.push_back(nums[index]);
           sum = sum + nums[index];
           backtrack(sum, numbers, index, target, result, nums);

           // don't include
           numbers.pop_back();
           sum = sum - nums[index];
           backtrack(sum, numbers, index + 1, target, result, nums);
        }



    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        // input vector nums
        vector<vector<int>> result{};
        vector<int> numbers{};
        backtrack(0, numbers, 0, target, result, nums);
        
        return result;
    }
};
