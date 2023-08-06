
/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {

    const ROWS = board.length;
    const COLS = board[0].length;

    function rec(row, col, idx, paths=null){

        if (paths===null){
            paths = new Set();
        }

        if (idx === word.length){
            return true;
        }
        if (
            paths.has(`${row},${col}`) ||
            row < 0 ||
            col < 0 ||
            row >= ROWS ||
            col >= COLS
        ){
            return false;
        }
        if (word[idx] == board[row][col]){
            paths.add(`${row},${col}`)
            res = (
                rec(row+1, col, idx+1, paths)  ||
                rec(row-1, col, idx+1, paths)  ||
                rec(row, col+1, idx+1, paths)  ||
                rec(row, col-1, idx+1, paths) 
            )
            paths.delete(`${row},${col}`)
            return res
        }
        return false
    }
    
    for (let row=0; row < ROWS; row++){
        for(let col=0; col < COLS; col++){
            if (rec(row, col, 0)){
                return true;
            }
        }
    }
    return false
};







const board = [
    Array.from("SIEE"),
    Array.from("SFMS"),
    Array.from("ONAE")
  ];
  const words = ["SIEMANO", "SIEMA", "SIEMU"];
  

  // Print the board
  board.forEach(row => {
    console.log(row.join(' '));
  });
  
  // Print the words and whether they exist on the board
  words.forEach(word => {
    console.log("Word:", word);
    // Call the exist method and print the result (implement the exist method within the Solution class)
    console.log(`word_exist ${exist(board, word)}`);
  });