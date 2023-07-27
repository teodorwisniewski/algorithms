

class ListNode {
    constructor(val=0, next=null) {
        this.val = val;
        this.next = next;
    }
}

function printList(node) {
    let currentNode = node;
    while(currentNode !== null) {
        process.stdout.write(currentNode.val + " ");
        currentNode = currentNode.next;
    }
    console.log();
}


// /**
//  * @param {ListNode} list1
//  * @param {ListNode} list2
//  * @return {ListNode}
//  */
// var mergeTwoLists = function(list1, list2) {
    
//     if (list1 === null){
//         return list2;
//     } else if(list2===null){
//         return list1;
//     } else if (list1.val < list2.val){
//         list1.next = mergeTwoLists(list1.next, list2);
//         return list1;
//     } else{
//         list2.next =  mergeTwoLists(list1, list2.next);
//         return list2
//     }
// };

/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    
    let mergedHead = {val:null, next:null};
    let curr = mergedHead;
    while(list1 && list2){
        if (list1.val < list2.val){
            curr.next = list1;
            list1 = list1.next;
        } else{
            curr.next = list2;
            list2 = list2.next;
        }
        curr = curr.next
    }
    curr.next = list1 || list2

    return mergedHead.next
};



// Creating the first list [1, 2, 4]
let list1_node1 = new ListNode(4);
let list1_node2 = new ListNode(2, list1_node1);
let list1 = new ListNode(1, list1_node2); // This is the head of the first list

// Creating the second list [1, 3, 4]
let list2_node1 = new ListNode(4);
let list2_node2 = new ListNode(3, list2_node1);
let list2 = new ListNode(1, list2_node2); // This is the head of the second list

// Now let's print our lists
process.stdout.write("List 1: ");
printList(list1);

process.stdout.write("List 2: ");
printList(list2);


let res = mergeTwoLists(list1, list2);
console.log(`mergeTwoLists`);
printList(res);
