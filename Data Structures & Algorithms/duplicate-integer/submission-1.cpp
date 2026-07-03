class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        vector<int> seen;

        for (int i = 0; i < nums.size(); i++) {
            if (find(seen.begin(), seen.end(), nums[i]) != seen.end()) {
                return true;
            }
            seen.push_back(nums[i]);
        }

        return false;
    }
};
