






var exist = function(board, word) {

    const ROWS = board.length;
    const COLS = board[0].length;

    function backtrack(row, col, wordIdx, paths=null){

        if (paths===null){
            paths = new Set();
        }
        
        if (wordIdx === word.length){
            return true;
        }
        let row_col_combo = `${row},${col}`;
        cond = (
            paths.has(row_col_combo) || 
            row < 0 ||
            row >= ROWS ||
            col < 0 ||
            col >= COLS
        )
        if (cond){
            return false;
        }

        if (word[wordIdx] == board[row][col]){
            paths.add(row_col_combo);
            res = (
                backtrack(row+1, col, wordIdx+1, paths) ||
                backtrack(row-1, col, wordIdx+1, paths) ||
                backtrack(row, col+1, wordIdx+1, paths) ||
                backtrack(row, col-1, wordIdx+1, paths)
            )
            paths.delete(row_col_combo);
            return res
        }
        return false;
    }

    for (let col=0; col < COLS; col++){
        for (let row=0; row < ROWS; row++){
            if (backtrack(row, col, 0)){
                return true;
            }
        }
    }
    return false;
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

  let board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
  let word2 = "ABCB"
  console.log("word2:", word2);
   // Print the board
   board2.forEach(row => {
    console.log(row.join(' '));
  });
  console.log(`word_exist expect false and obtained: ${exist(board2, word2)}`);