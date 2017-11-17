class Solution {
public:
    typedef vector<vector<int>> ListOfList;
    void recursion(vector<int> &path, vector<int> &remain, int k, int n, ListOfList &ans){
        if(k == 0){
            if(n == 0)
                ans.push_back(path);
        }else{
            for(int i = 0; i < remain.size() && remain[i] <= n; ++i){
                auto newPath = path;
                newPath.push_back(remain[i]);
                vector<int> newRemain(remain.begin()+i+1, remain.end());
                recursion(newPath, newRemain, k - 1, n - remain[i], ans);
            }
        }
    }
    ListOfList combinationSum3(int k, int n) {
        ListOfList ans;
        vector<int> path;
        vector<int> remain;
        for(int i = 1; i < 10 && i < n; ++i)
            remain.push_back(i);
        recursion(path, remain, k, n, ans);
        return ans;
    }
};