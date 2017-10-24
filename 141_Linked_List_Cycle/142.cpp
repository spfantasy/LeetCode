/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        // use two pointers
        ListNode *ptr1 = head;
        ListNode *ptr2 = head;
        while(ptr1 != nullptr && ptr1->next != nullptr){
            // 2 step / 1 step at each time
            ptr1 = ptr1->next->next;
            ptr2 = ptr2->next;
            // if there's a cycle, they'll meet finally
            if(ptr1 == ptr2)
                return true;
        }
        return false;
    }
};