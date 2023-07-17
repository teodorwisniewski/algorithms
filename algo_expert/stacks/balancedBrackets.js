

const closingBrackets = [')', ']', '}'];
const openingBrackets = ['(', '[', '{'];
const bracketPairs = {
    '(': ')',
    '[': ']',
    '{': '}'
}

// TC O(n) SC O()
function balancedBrackets(string) {
    let stack = [];
    for (let i=0; i<string.length; i++){
        ch = string[i];
        // finding closing bracket
        if (closingBrackets.includes(ch))
        {
            lastStackElement = stack.pop();
            if (bracketPairs[lastStackElement] !== ch)
            {
                return false
            }
        } else if (openingBrackets.includes(ch)){
            stack.push(ch);
        }
    } 
    if (stack.length > 0){
        console.log(`The stack is not empty ${stack} and has : ${stack.length} elements.`);
        return false
    }
    return true
        
  }
  



let text = "([])(){}(())()()"

console.log(`The input text ${text} is balanced: ${balancedBrackets(text)}`);


text2 = "()[]{}{"

console.log(`\n The input text2 ${text2} is balanced: ${balancedBrackets(text2)}`);


text2 = "(a)"

console.log(`\n The input text2 ${text2} is balanced: ${balancedBrackets(text2)}`);