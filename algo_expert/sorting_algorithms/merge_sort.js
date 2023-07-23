


// TC O(n * logn) SC O(n)
function mergeSort(arr){

    if (arr.length === 1){
        return arr;
    }

    let midPoint = Math.floor(arr.length / 2)
    let left = arr.slice(0, midPoint)
    let right = arr.slice(midPoint)

    console.log(`Left side ${left}`);
    console.log(`Right side ${right}`);

    return merge(
        mergeSort(left),
        mergeSort(right)
    )
}


function merge(left, right){
    let outputArr = []
    let leftIdx = 0;
    let rightIdx = 0;
    while (leftIdx < left.length  && rightIdx < right.length){
        if (left[leftIdx] <= right[rightIdx]){
            outputArr.push(left[leftIdx]);
            leftIdx++;
        } else{
            outputArr.push(right[rightIdx]);
            rightIdx++;
        }
    }
    
    let mergedArr = outputArr.concat(left.slice(leftIdx)).concat(right.slice(rightIdx))
    console.log(`merge Right side ${right} and Left side ${left}`);
    console.log(`mergedArr ${mergedArr}`);
    return mergedArr
}










let unsortedArray = [7, 3, 1, 4 ,2];
console.log(`Unsorted array ${unsortedArray}`)
console.log(`Sorted array mergeSort ${mergeSort(unsortedArray)}`)