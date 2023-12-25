

function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}





var sumNumbers = function(root) {
    let res = sumNumbersHelper(root, 0);
    return res
};


function sumNumbersHelper(root, branch_num){
    if (root === null){
        return 0
    }
    branch_num = branch_num * 10 + root.val;
    if (root.left === null && root.right === null){
        return branch_num;
    }
    return sumNumbersHelper(root.left, branch_num) + sumNumbersHelper(root.right, branch_num);
}







// Construct the tree
// Construct the tree
const root = new TreeNode(1);
root.left = new TreeNode(2);
root.right = new TreeNode(3);


let res = sumNumbers(root)
console.log(`sumNumbers for input [1, 2, 3] is ${res}`)