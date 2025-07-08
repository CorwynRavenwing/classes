/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    let function_cache = {}
    
    return function(...args) {

        key = args.join()
        console.log("function has args:", args, "key:", key)
        if (key in function_cache) {
            answer = function_cache[key]
            console.log("  Cache hit:", answer)
        } else {
            console.log("  Cache miss:")
            answer = fn(...args)
            console.log("  ...", answer)
            function_cache[key] = answer
        }
        return answer
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */

// NOTE: Accepted on third Run (several JS issues)
// NOTE: Accepted on first Submit
// NOTE: Runtime 937 ms Beats 5.15%
// NOTE: Memory 90.32 MB Beats 99.94%
