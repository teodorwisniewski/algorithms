

function numberOfWaysToMakeChange(n, denoms) {
    
    let ways = new Array(n+1).fill(0);
    ways[0] = 1;
    for (denom of denoms){
        for (amount=1;amount<n+1;amount++){
            if (denom <= amount){
                ways[amount] += ways[amount-denom];
            }
        }
    }
    return ways[ways.length - 1]
  }




const denoms = [1, 5, 10];
const target = 10;
const res = numberOfWaysToMakeChange(target, denoms);

console.log(`denoms ${denoms} target=${target}`);
console.log(`numberOfWaysToMakeChange ${res}`);