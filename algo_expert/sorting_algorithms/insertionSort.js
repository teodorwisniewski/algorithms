


function swap(array, i, j){
    let temp = array[i];
    array[i] = array[j];
    array[j] = temp;
}


function insertionSort(array) {
    for (let i=1; i<array.length; i++){
        j = i;
        while(j>0 && array[j] < array[j-1]){
            swap(array, j, j-1);
            j -= 1;
        }
    }
    return array
  }
  








let unsortedArray = [7 ,3 ,1 ,4 ,2];
console.log(`Unsorted array ${unsortedArray}`)
console.log(`Sorted array ${insertionSort(unsortedArray)}`)