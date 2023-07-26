

function quickSort(arr){
    quickSortHelper(arr, 0, arr.length-1);
    return arr;
}


function quickSortHelper(arr, startIdx, endIdx){

    if (startIdx >= endIdx) return;
        
    
    let pivotIdx = getPivot(arr, startIdx, endIdx);
    let isLeftSubarraySmaller = pivotIdx - startIdx - 1 < endIdx - (pivotIdx+1)
    if (isLeftSubarraySmaller){
        quickSortHelper(arr, startIdx, pivotIdx-1);
        quickSortHelper(arr, pivotIdx+1, endIdx);
    } else{
        quickSortHelper(arr, pivotIdx+1, endIdx);
        quickSortHelper(arr, startIdx, pivotIdx-1);
    }
}


function getPivot(arr, startIdx, endIdx){

    let leftIdx = startIdx + 1;
    let rightIdx = endIdx;
    let pivotIdx = startIdx;
    let pivotVal = arr[pivotIdx];
    while(leftIdx <= rightIdx){
        if (arr[leftIdx] > pivotVal && arr[rightIdx] < pivotVal){
            swap(arr, leftIdx, rightIdx);
        }
        if(arr[leftIdx] <= pivotVal) leftIdx++;
        if(arr[rightIdx] >= pivotVal) rightIdx--;
    }
    swap(arr, rightIdx, pivotIdx);
    return rightIdx;
}






function swap(array, i, j){
    temp = array[i];
    array[i] = array[j];
    array[j] = temp;
}





  let undsortedArray = [7 ,3 ,1 ,4 ,2];
  console.log(`Unsorted array ${undsortedArray}`)
  console.log(`Sorted array ${quickSort(undsortedArray)}`)


  undsortedArray = [5, 3, 1 ,4 ,0];
  console.log(`Unsorted array ${undsortedArray}`)
  console.log(`Sorted array ${quickSort(undsortedArray)}`)