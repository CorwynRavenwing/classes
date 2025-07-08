/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function(rowsCount, colsCount) {
    console.log("array", this)

    if (rowsCount * colsCount != this.length) {
        console.log("size", this.length, "!=", rowsCount, "*", colsCount)
        return []
    }

    function chunk(arr, chunkSize) {
        if (chunkSize <= 0) throw "Invalid chunk size";
        var R = [];
        for (var i=0,len=arr.length; i<len; i+=chunkSize)
            R.push(arr.slice(i,i+chunkSize));
        return R;
    }
    chunked = chunk(this, rowsCount)
    console.log("chunked", chunked)

    function reverse_every_other(arr) {
        R = []
        for (const [index, row] of arr.entries()) {
            if (index % 2 == 0) {
                R.push(row)
            } else {
                R.push(row.reverse())
            }
        }
        return R
    }
    reversed = reverse_every_other(chunked)
    console.log("reversed", reversed)

    function transpose(arr) {
        // iterate columns
        var R = arr[0].map(function (col, c) {
            // For each column, iterate all rows
            return arr.map(function (row, r) { 
                return arr[r][c]; 
            }); 
        });
        return R
    }
    transposed = transpose(reversed)
    console.log("transposed", transposed)

    return transposed
}

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */

// NOTE: Accepted on first Run
// NOTE: Accepted on first Submit
// NOTE: Runtime 417 ms Beats 5.06%
// NOTE: Memory 78.96 MB Beats 5.06%
