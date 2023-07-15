
function swap(array, i, j){
    temp = array[i];
    array[i] = array[j];
    array[j] = temp;
}



function bubbleSort(array) {
    let isSorted = false;
    lastIndex = array.length - 1
    while (!isSorted){
        isSorted = true
        for (let i=0; i<lastIndex; i++){
            if(array[i] > array[i+1]){
                swap(array, i, i+1)
                isSorted = false
            }
        }
    }
    return array;
  }


  let undsortedArray = [7 ,3 ,1 ,4 ,2];
  console.log(`Unsorted array ${undsortedArray}`)
  console.log(`Sorted array ${bubbleSort(undsortedArray)}`)