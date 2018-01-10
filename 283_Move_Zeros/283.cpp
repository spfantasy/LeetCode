#include <iostream>
#include <vector>
#include <numeric>
#include <string>
#include <functional>
using namespace std;
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        auto eos = nums.begin();
        auto itr = nums.begin();
        while(itr != nums.end()){
            if(*itr == 0){
                ++itr;
            }else{
                if(itr != eos){
                    swap(*itr, *eos);
                }
                ++itr;
                ++eos;
            }
        }
    }
};

int main(){
	Solution *A;
	std::vector<int> B = {0};
	A->moveZeroes(B);
	for(auto &e : B) cout<<e<<endl;
}