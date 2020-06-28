class Solution:
    def ReverseList(self,pHead):
        pReverseHead = None
        pNode = pHead
        pPre = None
        while pNode != None:
            pNext = pNode.next
            if pNext == None:
                pReverseHead = pNode
            pNode.next = pPre
            pPre = pNode
            pNode = pNext
        return pReverseHeads

''''
反转链表
'''
'''
/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode(int x) { val = x; }
 * }
 */
'''
class Solution {
    public ListNode reverseList(ListNode head) {
 if(head == null || head.next == null)
 return head;
 ListNode pre = head;
 ListNode pNode = head.next;
 ListNode next = head;
 //首先处理前两个节点；
 pre.next = null;
 while(pNode != null)
 {
 next = pNode.next;
 pNode.next = pre;
 pre = pNode; //就是pre和pNode同时往后面进行移动；
 pNode = next; //就是pre和pNode同时往后面进行移动；
 }
 return pre;
 }
}

