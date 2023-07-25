

// TC O(n log n) SC O(log n) 
function quickSort(array) {
    quickSortHelper(array, 0, array.length-1);
    return array;
}


// function quickSortHelper(array, startIdx, endIdx){

//     if (startIdx >= endIdx){
//         return;
//     }
//     let pivotIdx = getPivot(array, startIdx, endIdx)

//     let isLeftSubarraySmaller = pivotIdx - startIdx - 1 < endIdx - (pivotIdx + 1)
//     if (isLeftSubarraySmaller){
//         quickSortHelper(array, 0, pivotIdx-1);
//         quickSortHelper(array, pivotIdx+1, endIdx);
//     } else{
//         quickSortHelper(array, pivotIdx+1, endIdx);
//         quickSortHelper(array, 0, pivotIdx-1);        
//     }
// }


function quickSortHelper(array, startIdx, endIdx) {
    if (startIdx >= endIdx) {
        return;
    }
    let pivotIdx = getPivot(array, startIdx, endIdx);
    quickSortHelper(array, startIdx, pivotIdx - 1);
    quickSortHelper(array, pivotIdx + 1, endIdx);
}


function getPivot(array, startIdx, endIdx){

    let pivotIdx = startIdx;
    let pivotValue = array[startIdx]
    let leftIdx = startIdx + 1;
    let rightIdx = endIdx;
    while (leftIdx <= rightIdx){
        if (array[leftIdx] > pivotValue && array[rightIdx] < pivotValue){
            swap(array, leftIdx, rightIdx);
        }
        if(array[leftIdx] <= pivotValue){
            leftIdx++;
        }
        if(array[rightIdx] >= pivotValue){
            rightIdx--;
        }
    }
    swap(array, pivotIdx, rightIdx);
    return rightIdx;
}


function swap(array, i, j){
    temp = array[i];
    array[i] = array[j];
    array[j] = temp;
}


// Do not edit the line below.
exports.quickSort = quickSort;


  let undsortedArray = [7 ,3 ,1 ,4 ,2];
  console.log(`Unsorted array ${undsortedArray}`)
  console.log(`Sorted array ${quickSort(undsortedArray)}`)


  undsortedArray = [5, 3, 1 ,4 ,0];
  console.log(`Unsorted array ${undsortedArray}`)
  console.log(`Sorted array ${quickSort(undsortedArray)}`)