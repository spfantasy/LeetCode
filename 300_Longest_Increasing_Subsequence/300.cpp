class Solution {
public:
    int BinarySearch(vector<int> &lst, int num){
        if(lst.size() == 0) return -1;
        auto start = lst.begin();
        auto end = lst.end()-1;
        while(start + 1 < end){
            auto mid = start + (end - start)/2;
            if(*mid >= num){
                end = mid;
            }else{
                start = mid;
            }
        }
        if(*end < num) return end - lst.begin();
        else if(*start < num) return start - lst.begin();
        else return -1;
    }
    int lengthOfLIS(vector<int>& nums) {
        vector<int> LeastEndingWithLength;
        for(auto &num: nums){
            int place = BinarySearch(LeastEndingWithLength,num) + 1;
            if(place >= LeastEndingWithLength.size()){
                LeastEndingWithLength.push_back(num);
            }else{
                LeastEndingWithLength[place] = min(LeastEndingWithLength[place],num);
            }
        }
        // for(auto &e:LeastEndingWithLength) cout<<e<<',';
        return LeastEndingWithLength.size();
    }
};