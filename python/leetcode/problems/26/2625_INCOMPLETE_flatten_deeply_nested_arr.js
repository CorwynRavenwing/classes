/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {

    var flatten_fn = function (total, value, index, arr) {
        // console.log('flatten_fn()', total, value)
        if (Array.isArray(value)) {
            value.forEach(
                V => total.push(V)  // array: push each member onto list
            )
            // console.log('  array:', total)
            return total
        } else {
            total.push(value)       // not array: push onto list as-is
            // console.log('  not array:', total)
            return total
        }
    };

    while (n) {
        // console.log('flat()', arr, n)
        arrays_flattened = 0

        if (! Array.isArray(arr)) {
            console.log('  arr IS NOT an array !!!')
            return []
        }

        new_arr = arr.reduce(flatten_fn, [])
        if (new_arr == arr) {
            console.log('  No change! n =', n)
            return arr
        }
        arr = new_arr
        n -= 1
    }
    // console.log('  return as-is')
    return arr
};

// NOTE: times out for large inputs.
// NOTE: there is likely a better solution using Slice() instead.
