class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        //Boyer-Moore voting algorithm
        vector<int> ans;
        int v1 = 0, c1 = 0, v2 = 0, c2 = 0;
        //get possible value of >1/3 item
        for(auto &num : nums){
            if(num == v1)
                ++c1;
            else if(num == v2)
                ++c2;
            else if(c1 == 0){
                v1 = num;
                ++c1;
            }else if(c2 == 0){
                v2 = num;
                ++c2;
            }
            else{
                --c1;
                --c2;
            }
        }
        if(count(nums.cbegin(), nums.cend(), v1) * 3 > nums.size())
            ans.push_back(v1);
        if(count(nums.cbegin(), nums.cend(), v2) * 3 > nums.size())
            ans.push_back(v2);
        if(ans.size() == 2 && ans[0] == ans[1])
            ans.pop_back();
        return ans;
    }
};