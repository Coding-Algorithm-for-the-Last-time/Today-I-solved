// Runtime 53 ms Beats 93.60%
// Memory 41.6 MB Beats 99.20%

var minimumCost = function(cost) {
    cost.sort((a,b)=>b-a)
    var result = 0
    var costLen = cost.length

    for (var i=0; i<costLen; i++){
        if (i%3===2) continue
        result += cost[i]
    }

    return result
};