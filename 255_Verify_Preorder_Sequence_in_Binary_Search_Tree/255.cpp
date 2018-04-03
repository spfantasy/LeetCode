#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <unordered_map>
#include <queue>
using namespace std;

class Task{
public:
    int start;
    int end;
    Task(int s, int e): start(s), end(e){}
};

class Solution {
public:
    bool verifyPreorder(vector<int>& preorder) {
        queue<Task> tasks;
        tasks.push(Task(0,preorder.size()));
        while(tasks.size() > 0){
        	//get the first element in queue
        	auto current_task = tasks.front();
        	tasks.pop();
        	//only judge when length >= 2
        	if(current_task.end - current_task.start > 2){
        		//value that seperate two branch
        		int thres = preorder[current_task.start];
        		//a flag to split left and right
        		int first_element_greater = current_task.end;
        		//set the flag
        		for(int i = current_task.start + 1; i < current_task.end; ++i){
        			if(preorder[i] > thres){
        				first_element_greater = i;
        				break;
        			}
        		}
        		//ensure nothing right than flag disobey the rule
        		for(int i = first_element_greater; i < current_task.end; ++i){
        			if(preorder[i] < thres){
        				return false;
        			}
        		}
        		//set two child tasks
        		tasks.push(Task(current_task.start + 1, first_element_greater));
        		tasks.push(Task(first_element_greater, current_task.end));
        	}
        }
        return true;
    }
};



int main(){
	Solution *s;
	vector<int> v = {5,1,7,4,6};
	cout<<s->verifyPreorder(v);
}