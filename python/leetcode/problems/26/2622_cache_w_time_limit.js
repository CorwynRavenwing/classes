var TimeLimitedCache = function() {
    // 'key': 'value'
    cache_object = {};
    // 'key': timeoutID
    cache_timeoutIDs = {};
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    // console.log(cache_object)
    if (key in cache_object) {
        console.log("key", key, "found");
        answer = true;
        console.log("  clearing old timeout for key", key);
        clearTimeout(cache_timeoutIDs[key]);
    } else {
        console.log("key", key, "not found");
        answer = false;
    }
    cache_object[key] = value;
    cache_timeoutIDs[key] = setTimeout(() => {
        console.log("key", key, "auto-deleted after time", duration);
        delete cache_object[key];
    }, duration);
    console.log("key", key, "set to value", value, "for time", duration);
    return answer;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    if (key in cache_object) {
        value = cache_object[key]
        console.log("key", key, "fetched", value)
        return value
    } else {
        console.log("key", key, "NOT FOUND")
        return -1
    }
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    // return cache_object.length
    return Object.keys(cache_object).length
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */

// NOTE: Accepted on fifth Run (several JS issues)
// NOTE: Accepted on first Submit
// NOTE: Runtime 49 ms Beats 41.81%
// NOTE: Memory 53.45 MB Beats 49.16%
