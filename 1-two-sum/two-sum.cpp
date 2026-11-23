class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int , int> hashMap;
        for (int i = 0 ; i < nums.size() ; ++i){
            int difference = target - nums[i];
            if (!hashMap.contains(difference)){
                hashMap[nums[i]] = i;
            }
            else{
                return {hashMap[difference],i};
            }
        }
    return {};
    }
};