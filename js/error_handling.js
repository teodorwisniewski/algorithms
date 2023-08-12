

var expect = function(val) {
    

    return {
        expectedValue: val,
        toBe: function(val) {
            if (this.expectedValue === val){
                return true;
            }
            throw new Error("Not Equal")
        },
        notToBe: function(val) {
            if (this.expectedValue !== val){
                return true;
            }
            throw new Error("Equal")
        },
    }
};
