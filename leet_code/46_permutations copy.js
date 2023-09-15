


// TC O(n * n!) SC O(n * n!)
var permute = function(nums) {
    let perms = []
    let currPerm = Array(nums.length).fill("0")
    permuteHelper(0, perms, nums);
    return perms;
};


function permuteHelper(idx, perms, nums){
    if (idx === nums.length - 1){
        perms.push(nums.slice());
    } else{
        for (let i=idx; i< nums.length; i++){
            swap(nums ,idx ,i);
            permuteHelper(idx+1, perms, nums)
            swap(nums ,i ,idx);
        }
    }
}

function swap(arr, i, j){
    let temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}


let inputArray = ["A", "B", "C"];

let perms = permute(inputArray);

for (let i=0; i<perms.length; i++){
    perm = perms[i];
    console.log(`${i} the perm goes as follows ${perm}`)
}