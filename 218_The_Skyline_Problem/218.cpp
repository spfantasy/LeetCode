class Solution {
public:
    vector<pair<int, int>> getSkyline(vector<vector<int>>& buildings) {
        vector<pair<int, int>> ans;
        //get all possible points
        unordered_set<int> x_set;
        for(auto &building : buildings){
            x_set.insert(building[0]);
            x_set.insert(building[1]);
        }
        vector<int> x_list(x_set.begin(), x_set.end());
        std::sort(x_list.begin(), x_list.end());
        //iterate through all possible xs'
        priority_queue<pair<int,int>> h_r;
        int itr = 0;
        for(auto &x : x_list){
            //push all building started to heap
            while(itr < buildings.size()){
                if(buildings[itr][0] <= x){
                    h_r.push(make_pair(buildings[itr][2], buildings[itr][1]));
                    ++itr;
                }
                else
                    break;
            }
            //pop from top to ensure the highest building in heap still exist
            while(!h_r.empty()){
                if(h_r.top().second <= x)
                    h_r.pop();
                else
                    break;
            }
            //insert only when height changes
            int h = h_r.empty() ? 0 : h_r.top().first;
            if(ans.size() == 0 || h != ans.back().second)
                ans.push_back(make_pair(x, h));
        }
        return ans;
    }
};