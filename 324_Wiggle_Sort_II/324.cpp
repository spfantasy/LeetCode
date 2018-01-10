class Solution {
public:
    int &val(vector<int>& nums, int i){
        int n = nums.size();
        int new_idx = 1+i*2;
        if(new_idx >= n){//7 1,3,5,0,2,4,6
            new_idx -= int(n/2)*2+1;
        }
        return nums[new_idx];
        // return nums[(1+2*(i))%(n|1)];
    }
    void wiggleSort(vector<int>& nums) {
        int n = nums.size();
        auto midptr = nums.begin() + n/2;
        nth_element(nums.begin(),midptr,nums.end());
        int mid = *midptr;
        int i = 0;//last of elements > mid
        int j = 0;//last of elements = mid
        int k = n-1;//first of elements < mid
        // #define val(i) nums[(1+2*(i))%(n|1)]
        while(j <= k){
            if(val(nums, j) > mid){
                swap(val(nums, i++),val(nums, j++));
            }else if(val(nums, j) < mid){
                swap(val(nums, j),val(nums, k--));
            }else{
                j++;
            }
        }
    }
};
