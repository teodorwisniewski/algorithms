var createCounter = function(init) {
    count = init;
    
    return {
        increment: () => {
            count += 1;
            return count;
        },

        decrement: () => {
            count -= 1;
            return count;
        },

        reset: () => {
            count = init;
            return count;
        }
    }
};