var numRabbits = function(answers) {
    let result = 0
    const cnt = {}
    answers.forEach(v=>cnt[v] = v in cnt? cnt[v] + 1 : 1)
    Object.entries(cnt).forEach(([k,v])=>{
        k = parseInt(k)
        result+=Math.ceil(v/(k+1))*(k+1)
    })
    return result
};