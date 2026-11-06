class Solution {
public:
    int minMoves(vector<int>& nums) {
        auto maxValues = max_element(nums.begin(),nums.end()); // this line basically gives me a pointer where the max values is stored in the memory
        auto maxValue = *maxValues; // this line dereferences the pointer to fetch the value that is stored in that pointer
        int count = 0;
        for (size_t i = 0 ; i < nums.size(); i++){
            
            count += maxValue - nums[i];
        }
        return count;
    }
};