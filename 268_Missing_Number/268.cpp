#include <iostream>
#include <vector>
#include <numeric>
#include <string>
#include <functional>
using namespace std;
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        return (*std::min_element(nums.begin(),nums.end())+*std::max_element(nums.begin(),nums.end()))*(nums.size()+1)/2 - std::accumulate(nums.begin(),nums.end(),0);
    }
};

int main(){
	Solution *A;
	std::vector<int> B = {1,3,0};
	cout<<A->missingNumber(B);
}