/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
    
    let timeoutID = null

    return function(...args) {
        if (timeoutID != null) {
            clearTimeout(timeoutID)
        }
        timeoutID = setTimeout(fn, t, ...args)
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */

// NOTE: Runtime 60 ms Beats 50.92%
// NOTE: Memory 49.30 MB Beats 44.28%
