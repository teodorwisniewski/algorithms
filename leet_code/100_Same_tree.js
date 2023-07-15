


function TreeNode(val, left, right) {
         this.val = (val===undefined ? 0 : val)
         this.left = (left===undefined ? null : left)
         this.right = (right===undefined ? null : right)
     }

var isSameTree = function(p, q) {
    
    if (p===null && q===null){
        return true;
    }else if (p===null || q===null){
        return false;
    }

    
    if (p.val === q.val){
        return isSameTree(p.right, q.right) && isSameTree(p.left, q.left)
    }
    
    return false
};


// Tworzenie przykładowego drzewa binarnego
const node1 = new TreeNode(1);
const node2 = new TreeNode(2);
const node3 = new TreeNode(3);
const node4 = new TreeNode(4);
const node5 = new TreeNode(5);

node1.left = node2;
node1.right = node3;
node2.left = node4;
node2.right = node5;


    //      1
    //    /   \
    //   2     3
    //  / \
    // 4   5

// Funkcja wypisująca wartości drzewa w sposób przypominający strukturę drzewa
function printTree(node, indent = '') {
  if (node === null) {
    console.log(indent + 'null');
    return;
  }

  console.log(indent + node.val);
  printTree(node.left, indent + '  ├─ ');
  printTree(node.right, indent + '  └─ ');
}

// Wywołanie funkcji printTree dla utworzonego drzewa
printTree(node1);

// console.log(`cond ${isSameTree(node1, node1)} `)
// console.log(`cond ${isSameTree(node1, node2)} `)


const node11 = new TreeNode(0);
const node22 = new TreeNode(-8);
node11.left = node22;
const node111 = new TreeNode(0);
const node222 = new TreeNode(-5);
node111.left = node222;
console.log(`cond ${isSameTree(node11, node111)} `)


