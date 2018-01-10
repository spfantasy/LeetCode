#include <vector>
using namespace std;
class Solution {
public:
    int MaxSquareEndsIn(vector<vector<char>>& matrix, vector<vector<int>>& record, int x, int y){
        if(x < 0 || y < 0)
            return 0;
        else{
            if(record[x][y] == -1){
                if(matrix[x][y] == '0')
                    record[x][y] = 0;
                else
                    record[x][y] = min(min(MaxSquareEndsIn(matrix, record, x-1, y),
                                    MaxSquareEndsIn(matrix, record, x, y-1)),
                                    MaxSquareEndsIn(matrix, record, x-1, y-1))+1;
                return record[x][y];
            }
        }
    }
    int maximalSquare(vector<vector<char>>& matrix) {
        vector<vector<int>> record(matrix.size(), vector<int>(matrix[0].size(), -1));
        int ans = 0;
        for(int i = 0; i < matrix.size(); ++i){
            for(int j = 0; j < matrix[0].size(); ++j){
                ans = max(ans, MaxSquareEndsIn(matrix, record, i, j));
            }
        }
        return ans * ans;
    }
};