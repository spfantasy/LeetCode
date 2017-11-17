//std没有对unordered_set实现hash函数
//需要自己实现并放入unordered_set的template
struct pairhash {
public:
  template <typename T, typename U>
  std::size_t operator()(const std::pair<T, U> &x) const
  {
    return std::hash<T>()(x.first) * 31 + std::hash<U>()(x.second);
  }
};
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        //walk all the connected earth
        queue<pair<int, int>> Q;
        //the earth that has been searched
        unordered_set<pair<int, int>, pairhash> used;
        //direction matrix
        vector<int> x_ = {1,0,-1,0};
        vector<int> y_ = {0,1,0,-1};
        //special case
        int row = grid.size();
        if(row == 0)
            return 0;
        int col = grid[0].size();
        if(col == 0)
            return 0;
        int ans = 0;
        //core
        for(int i = 0; i < row; ++i){
            for(int j = 0; j <col; ++j){
                auto point = make_pair(i, j);
                //is this point earth that never been searched?
                if(used.find(point) == used.end() && grid[i][j] == '1'){
                    Q.push(point);
                    used.insert(point);
                    ++ans;
                    //BFS for all earch near it 
                    while(Q.size() > 0){
                        auto node = Q.front();
                        Q.pop();
                        for(int k = 0; k < 4; ++k){
                            int xx = node.first + x_[k];
                            int yy = node.second + y_[k];
                            auto newnode = make_pair(xx, yy);
                            //if new coordinate is valid and is earth and not searched
                            if(xx >= 0 && xx < row 
                               && yy >= 0 && yy < col 
                               && grid[xx][yy] == '1' 
                               && used.find(newnode) == used.end()){
                                Q.push(newnode);
                                used.insert(newnode);
                            }
                        } 
                    }
                }
            }
        }
        return ans;
    }
};