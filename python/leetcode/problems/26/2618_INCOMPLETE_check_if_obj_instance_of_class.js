/**
 * @param {*} obj
 * @param {*} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    target = classFunction.prototype
    console.log('target', target)
    console.log('obj', obj)
    while (obj != target) {
        obj = obj.__proto__
        console.log('obj', obj)
        if (obj == null) {
            return false
        }
    }
    return true
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */

// NOTE: failing on case 6 regarding Bigint
