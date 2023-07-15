

function swap(array, i, j){
    temp = array[i];
    array[i] = array[j];
    array[j] = temp;
}


var bubleSort = function(nums) {
    
    let isSorted = false;
    let lastIndx = nums.length-  1;
    while (!isSorted){
        isSorted = true;
        for (let j=0; j<lastIndx; j++){
            if(nums[j] > nums[j+1]){
                swap(nums, j, j+1);
                isSorted = false;
            }
        }
        lastIndx -= 1;
    }
    return nums;

};



let unsortedArray = [7 ,3 ,1 ,4 ,2];
console.log(`Unsorted array ${unsortedArray}`)
console.log(`Sorted array ${bubleSort(unsortedArray)}`)