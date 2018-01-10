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
    ListNode *reverse(ListNode *head){
        ListNode *ptr = nullptr, *newhead = nullptr;
        while(head){
            newhead = head;
            head = head->next;
            newhead->next = ptr;
            ptr = newhead;
        }
        return newhead;
    }
    bool isPalindrome(ListNode* head) {
        bool retval = true;
        if(head == nullptr || head->next == nullptr) return true;
        //let fast always be a valid pointer
        //and slow's next is the next of latter half of LL(+1 if it is odd)
        ListNode *slow = head;
        ListNode *fast = head->next;
        //approch the middle point
        while(fast->next && fast->next->next){
            fast = fast->next->next;
            slow = slow->next;
        }
        //reverse latter part
        ListNode *head2 = reverse(slow->next);
        //see if they equal
        ListNode *p1 = head, *p2 = head2;
        while(p1 && p2){
            if(p1->val != p2->val){
                retval = false;
                break;
            }
            p1 = p1->next;
            p2 = p2->next;
        }
        //reverse the latter part back
        slow->next = reverse(head2);
        return retval;
    }
};