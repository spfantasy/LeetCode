#include <vector>
#include <string>
#include <bitset>
#include <cctype> 			//char 
#include <sstream>			//std::istringstream
#include <unordered_map>
#include <unordered_set>
#include <iostream>			//std::cin,std::cout
#include <unordered_map>
using namespace std;

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t ans = 0;
        for(int i = 0; i < 32; ++i){
            ans = (ans<<1) + (n&1);
            n = n>>1;
        }
        return ans;
    }
    //存在 O(lgn)的解法，先对前后两部分分别翻转，再对调前后两部分

};

int main(){
	Solution *A = new Solution();
    uint32_t src = 7;
	auto dst = A->reverseBits(src);
    cout<<bitset<32>(src)<<endl;
    cout<<bitset<32>(dst)<<endl;

	return 1;
}