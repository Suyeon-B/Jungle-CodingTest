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

var isPalindrome = (head) => {
    let arr = [];
    while(head!= null){
        arr.push(head.val);
        head = head.next;
    }
    while(arr.length > 1){
        if(arr.pop() !== arr.shift()){
            return false;
        }
    }
    return true;
};