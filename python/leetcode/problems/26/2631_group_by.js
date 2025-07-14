/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {

    retval = {};
    for (const item of this) {
        key = fn(item)
        console.log(item, key);
        if (!(key in retval)) {
            retval[key] = []
        }
        retval[key].push(item)
    }

    return retval;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */

// NOTE: Accepted on first Run
// NOTE: Accepted on first Submit
// NOTE: Runtime 651 ms Beats 5.30%
// NOTE: Memory 87.86 MB Beats 5.13%
