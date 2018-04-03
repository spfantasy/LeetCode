#include <string>
#include <iostream>
using namespace std;
int compare(int n1, int n2, int offset){
	int ans = 0;
	for(int i = 0; i < offset; ++i){
		n1 >>= 1;
		ans += count(n1 ^ n2)
	}
}
int compare(string &s1, string &s2){
	int max_offset = s1.size() - s2.size();
	int ans = 0;
	for(int offset = 0; offset <= max_offset; ++offset){
		for(int i = 0; i < s2.size(); ++i){
			if(s1[i+offset] != s2[i]){
				++ans;
			}
		}
	}
	return ans;
}
int main(){
	string s1,s2;
	cin >> s1;
	cin >> s2;
	//string s1 = "aaabb";
	//string s2 = "bab";
	cout<<(compare(s1,s2));
}