

// TC O(t-s) and SC O(t-s)
function blackjackProbability(target, startingHand) {
    let memo = {}
    return recHelper(target, startingHand, memo);
}


function recHelper(target, startingHand, memo){

    if (target-4 <= startingHand && startingHand <= target){
        return 0;
    } else if (startingHand in memo){
        return memo[startingHand];
    } 

    let totalProb = 0;
    let newStartingHand;
    for (let cartNb=1; cartNb<11; cartNb++){
        newStartingHand = cartNb + startingHand
        if (newStartingHand < target-4){
            totalProb += 0.1 * recHelper(target, newStartingHand, memo);
        } else if (newStartingHand > target){
            totalProb += 0.1
        }
    }
    memo[startingHand] = Number(totalProb.toFixed(3))
    return memo[startingHand];
}

  


let target = 21;
let startingHand = 15;
let res = blackjackProbability(target, startingHand);
console.log(`target=${target} startingHand=${startingHand}`);
console.log(`blackjackProbability ${res}`);

target = 100;
startingHand = 90;
res = blackjackProbability(target, startingHand);
console.log(`target=${target} startingHand=${startingHand}`);
console.log(`blackjackProbability ${res}`);