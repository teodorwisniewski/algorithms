class Node {
    constructor(name) {
      this.name = name;
      this.children = [];
    }
  
    addChild(name) {
      this.children.push(new Node(name));
      return this;
    }
  
    breadthFirstSearch(array) {
      let cur = this;
      let queue = [cur];    
      
      while (queue.length > 0){
        cur = queue.shift();
        array.push(cur.name)
        for (let child of cur.children){
            queue.push(child)
        }
      }
      return array;
    }
  }
  
  const nodesToIntroduce = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"];
  const root = new Node(nodesToIntroduce[0]);
  
  // Create level 2
  root.addChild(nodesToIntroduce[1]);
  root.addChild(nodesToIntroduce[2]);
  root.addChild(nodesToIntroduce[3]);
  
  // Create level 3
  root.children[0].addChild(nodesToIntroduce[4]);
  root.children[0].addChild(nodesToIntroduce[5]);
  root.children[1].addChild(nodesToIntroduce[6]);
  root.children[1].addChild(nodesToIntroduce[7]);
  root.children[2].addChild(nodesToIntroduce[8]);
  
  // Create level 4
  root.children[0].children[0].addChild(nodesToIntroduce[9]);
  root.children[0].children[1].addChild(nodesToIntroduce[10]);
  
  const res = root.breadthFirstSearch([]);
  console.log(`breadthFirstSearch ${res}`);
  