#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <unordered_map>
using namespace std;

class CrossBuilder{
private:
	unordered_map<int, vector<string>> dict;
public:
	CrossBuilder(){
		dict[1] = vector<string>{"o"};
	}
	void build(int num){
		if(dict.find(num-1) == dict.end()){
			build(num-1);
		}
		int offset = pow(3,num-2);
		for(auto &row : dict[num-1]){
			stringstream ss;
			for(int i = 0; i < offset; ++i){
				ss << ' ';
			}
			ss << row;
			dict[num].push_back(ss.str());
		}

		for(auto &row : dict[num-1]){
			stringstream ss;
			for(int loop = 0; loop < 3; ++loop){
				ss << row;
				if(loop != 2){
					for(int i = 0; i < offset - row.size(); ++i){
						ss << ' ';
					}
				}
			}
			dict[num].push_back(ss.str());
		}

		for(auto &row : dict[num-1]){
			stringstream ss;
			for(int i = 0; i < offset; ++i){
				ss << ' ';
			}
			ss << row;
			dict[num].push_back(ss.str());
		}

	}
	void print(int num){
		if(dict.find(num) == dict.end()){
			build(num);
		}
		for(auto &line : dict[num]){
			cout<<line<<endl;
		}
	}
};

int main(){
	int num = 1;
	CrossBuilder C;
	C.print(3);
	return 0;
}