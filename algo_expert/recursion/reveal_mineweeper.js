


function revealMinesweeper(board, row, col) {

    if (board[row][col] == 'M'){
        board[row][col] = 'X';
        return board;
    }
    let neighbors = get_point_neighbors(board, row, col);
    let nbAdjacentMines = getNbAdjancentMines(board, neighbors);
    board[row][col] = String(nbAdjacentMines);
    if (nbAdjacentMines === 0){
        for (const [newRow, newCol] of neighbors){
            if (board[newRow][newCol] === 'H'){
                board = revealMinesweeper(board, newRow, newCol);
            }
            
        }
    }

    return board;
}


function get_point_neighbors(board, row, col){
    const ROWS = board.length;
    const COLS = board[0].length;
    const dirs = generateDirections()
    let neighbors = [];
    for (const [rowDir, colDir] of dirs){
        const newRow = row + rowDir;
        const newCol = col + colDir;
        if(
            newRow >= 0 &&
            newCol >= 0 &&
            newRow < ROWS && 
            newCol < COLS
        ){
            neighbors.push([newRow, newCol]);
        }
    }
    return neighbors
}


function generateDirections(){
    let dirs = [];
    for (let i = -1; i <= 1; i++) {
        for (let j = -1; j <= 1; j++) {
            dirs.push([i, j]);
        }
    }
    dirs = dirs.filter(dir => !(dir[0] === 0 && dir[1] === 0))
    return dirs
}


function getNbAdjancentMines(board, neighbors){

    let nbAdjacentMines = 0;
    neighbors.forEach(neighbor => {
        const [newRow, newCol] = neighbor;
        if (board[newRow][newCol] === 'M'){
            nbAdjacentMines++;
        }
    })
    return nbAdjacentMines;
}
  


let board = [
    ["M", "M"],
    ["H", "H"],
    ["H", "H"]
  ];
  
  let row_nb = 2;
  let col_nb = 0;
  
  // Print the board
  board.forEach(row => {
    console.log(row.join(' '));
  });
  
  // Print the word
  console.log("row:", row_nb, " col:", col_nb);
  let output_board = revealMinesweeper(board, row_nb, col_nb);
  
  console.log("revealMinesweeper output");
  output_board.forEach(row => {
    console.log(row.join(' '));
  });
  
  let expected_output = [
    ["M", "M"],
    ["2", "2"],
    ["0", "0"]
  ];
  
  if (JSON.stringify(output_board) === JSON.stringify(expected_output)) {
    console.log('Output is correct');
  } else {
    console.log('Output is incorrect');
  }
  