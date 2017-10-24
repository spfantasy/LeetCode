class Solution {
public:
    int candy(vector<int>& ratings) {
        vector<int> answer(ratings.size(), 1);
        for(int i = 1; i < ratings.size(); ++i){
            if(ratings[i-1] < ratings[i])
                answer[i] = answer[i-1] + 1;
        }
        for(int i = ratings.size() - 2; i >= 0; --i){
            if(ratings[i] > ratings[i+1])
                answer[i] = max(answer[i], answer[i+1] + 1);
        }
        return accumulate(answer.begin(), answer.end(), 0);
    }
};