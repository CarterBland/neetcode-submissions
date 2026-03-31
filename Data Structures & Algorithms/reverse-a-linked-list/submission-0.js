/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @return {ListNode}
     */
    reverseList(head) {
        if (head === null || head.next === null) {
            return head;
        }

        const traverse = (currentNode, previousNode) => {
            if (currentNode.next !== null) {
                return traverse(currentNode.next, new ListNode(currentNode.val, previousNode));
            }
            return new ListNode(currentNode.val, previousNode);
        }
        
        return traverse(head.next, new ListNode(head.val));
    }
}

