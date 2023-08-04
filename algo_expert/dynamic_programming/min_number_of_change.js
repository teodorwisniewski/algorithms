
// TC O(n*d) SC O(n)
function minNumberOfCoinsForChange(n, denoms) {
  
    let minWays = new Array(n+1).fill(Infinity)
    minWays[0] = 0;
    for (let denom of denoms){
        for (let a=1;a<n+1;a++){
            if (a-denom<0) continue;
            minWays[a] = Math.min(minWays[a], minWays[a-denom]+1);
        }
    }
    if (minWays[n] === Infinity){
        return -1
    }else{
        return minWays[n]
    }
}


let denoms = [1, 5, 10];
let target = 10;
let res = minNumberOfCoinsForChange(target, denoms);

console.log(`denoms ${denoms} target=${target}`);
console.log(`minNumberOfCoinsForChange ${res}`);

denoms = [12, 13];
target = 10;
res = minNumberOfCoinsForChange(target, denoms);

console.log(`denoms ${denoms} target=${target}`);
console.log(`minNumberOfCoinsForChange ${res}`);