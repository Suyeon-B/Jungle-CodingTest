/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function(head) {
    let arr = [];
    while (head != null){
        arr.push(head.val);
        head = head.next;
    }
    let temp = [...arr].reverse();
    
    return JSON.stringify(arr) === JSON.stringify(temp)? true: false;
};