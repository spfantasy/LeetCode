/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        priority_queue<int, std::vector<int>, std::greater<int>> last;
        sort(intervals.begin(), intervals.end(),
            [](Interval a, Interval b){return a.start < b.start;});
        for(int i = 0; i < intervals.size(); ++i){
            if(last.empty()){
                last.push(intervals[i].end);
            }else{
                cout<<last.top()<<endl;
                if(last.top() <= intervals[i].start){
                    last.pop();
                }
                last.push(intervals[i].end);
            }
        }
        return last.size();
    }
};