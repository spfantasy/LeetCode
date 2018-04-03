#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <unordered_map>
using namespace std;
class Solution {
public:
    string encode(string &s){
        //assert(s.size() > 0);
        int offset = static_cast<int>(s[0]) - static_cast<int>('a');
        stringstream ss;
        for(auto &c : s){
            int digit = (static_cast<int>(c) - offset + 26) % 26;
            ss << static_cast<char>(digit);
        }
        return ss.str();
    }

    vector<vector<string>> groupStrings(vector<string> &strings) {
        unordered_map<string, vector<string>> classifier;
        for(auto &s : strings){
            classifier[this->encode(s)].push_back(s);
        }
        vector<vector<string>> output;
        for(auto &vec_of_string : classifier){
            output.push_back(vec_of_string.second);
        }
        return output;
    }
};