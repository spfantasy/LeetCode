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
    ListNode* insertionSortList(ListNode* head) {
        // fake start
        ListNode dummy(0);
        // head is the current node, move it till end(nullptr)
        while(head != nullptr){
            // the processing node
            ListNode *ptr = head;
            // move head 
            head = head->next;
            // insertion place
            ListNode *pos = &dummy;
            // move insertion place when next node is not None and smaller than it
            while(pos->next != nullptr && pos->next->val < ptr->val)
                pos = pos->next;
            // pos->ptr->pos.next
            ptr->next = pos->next;
            pos->next = ptr;
        }
        return dummy.next;
    }
};