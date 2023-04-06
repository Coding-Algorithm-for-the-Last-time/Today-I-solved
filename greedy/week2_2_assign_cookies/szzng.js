// Runtime 85 ms Beats 92.44%
// Memory 44.5 MB Beats 70%

var findContentChildren = function(g, s) {
    g.sort((a,b)=>b-a)
    s.sort((a,b)=>b-a)
    var end = Math.min(g.length, s.length)
    if (g.length>end) g.splice(0, g.length-end)
    if (s.length>end) s.splice(end)
    var result = 0
    var index = 0

    for (var i=0; i < end; i++){
        if (s.length ===0) return result

        if (s[index] >= g[i]){
            result+=1
            index+=1
        }
    }

    return result
};