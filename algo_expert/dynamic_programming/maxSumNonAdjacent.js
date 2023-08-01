


// TC O(n) SC O(n)
function maxSubsetSumNoAdjacent(array) {
    if (array.length === 0) return 0;
    if (array.length <= 2) return Math.max(...array);
    let maxSum = new Array(array.length).fill(0);
    maxSum[0] = array[0];
    maxSum[1] = Math.max(array[0], array[1]);
    for (let i=2; i<array.length; i++){
        first = maxSum[i-1];
        second = maxSum[i-2] + array[i];
        maxSum[i] = Math.max(first, second);
    }
    return maxSum[maxSum.length - 1]
  }


let arr = [75, 105, 120, 75, 90, 135];
let res = maxSubsetSumNoAdjacent(arr);
console.log(`maxSubsetSumNoAdjacent ${res} `);

arr2 = [1, 2];
res2 = maxSubsetSumNoAdjacent(arr2);
console.log(`maxSubsetSumNoAdjacent ${res2} `);

  