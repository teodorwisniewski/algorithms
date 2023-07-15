
function swap(array, i, j){
    temp = array[i];
    array[i] = array[j];
    array[j] = temp;
}


// TC O(n^2) SC O(1) 
function selectionSort(array) {

    for (let i=0; i<array.length; i++){
        let indexMinimalValue = i
        for(let j=i+1; j<array.length; j++){
            if(array[indexMinimalValue] > array[j]){
                indexMinimalValue = j;
            }
        }
        if (i !== indexMinimalValue){
           swap(array, i, indexMinimalValue);
        }
    }

    return array;
  }


  let undsortedArray = [7 ,3 ,1 ,4 ,2];
  console.log(`Unsorted array ${undsortedArray}`)
  console.log(`Sorted array ${selectionSort(undsortedArray)}`)