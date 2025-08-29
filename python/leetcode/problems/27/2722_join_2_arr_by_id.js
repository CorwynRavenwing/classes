/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    answer = []

    list1 = {}
    list2 = {}
    IDs1 = new Set()
    IDs2 = new Set()
    arr1.forEach( (ob) => { list1[ob.id] = ob; IDs1.add(ob.id); } )
    arr2.forEach( (ob) => { list2[ob.id] = ob; IDs2.add(ob.id); } )
    console.log('list1', list1)
    console.log('list2', list2)
    console.log('IDs1', IDs1)
    console.log('IDs2', IDs2)
    IDs = IDs1.union(IDs2)
    console.log('IDs', IDs)
    IDs = Array.from(IDs)
    // ... because OF COURSE we default to sorting numbers alphabetically !!!
    IDs.sort((a, b) => (a - b));
    console.log('IDs', IDs)

    IDs.forEach(
        (ID) => {
            console.log('ID:', ID)
            if (IDs1.has(ID)) {
                if (IDs2.has(ID)) {
                    console.log('  BOTH yes')
                    ob1 = list1[ID]
                    ob2 = list2[ID]
                    ob = ob1
                    for (const [key, value] of Object.entries(ob2)) {
                        console.log(`  ${key}: ${value}`);
                        if (key == 'id') {
                            console.log('    SKIP')
                            continue
                        }
                        if (ob.hasOwnProperty(key)) {
                            console.log('    Overwrite')
                        } else {
                            console.log('    New key')
                        }
                        // set the value in either case:
                        ob[key] = value
                    }
                    answer.push(ob)
                } else {
                    console.log('  arr1 yes')
                    ob = list1[ID]
                    answer.push(ob)
                }
            } else {
                if (IDs2.has(ID)) {
                    console.log('  arr2 yes')
                    ob = list2[ID]
                    answer.push(ob)
                }
            }
        }
    )

    return answer
};

// NOTE: Acceptance Rate 56.3% (medium)

// NOTE: Accepted on first Run
// NOTE: Accepted on second Submit (needed to override default sort [alphabetic !!!] with normal numeric sort)
// NOTE: Runtime 1717 ms Beats 5.04%
// NOTE: Memory 122.86 MB Beats 5.20%
