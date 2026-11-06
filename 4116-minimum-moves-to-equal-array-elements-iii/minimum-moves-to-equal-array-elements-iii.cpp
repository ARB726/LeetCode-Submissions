class Solution {
public:
    int minMoves(vector<int>& nums) {
        auto maxValues = max_element(nums.begin() , nums.end());
        auto maxValue = *maxValues;

        auto count = 0;

        for (size_t i = 0 ; i < nums.size(); i++){
            
            count += maxValue - nums[i];

        }
        return count;
    }
};