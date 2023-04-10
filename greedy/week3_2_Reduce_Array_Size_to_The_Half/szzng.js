var minSetSize = function(arr) {
    const cnt = {}
    arr.forEach(v=> {
        if (v in cnt) cnt[v]+=1
        else cnt[v]=1
    })

    const frequency = Object.values(cnt).sort((a,b)=>b-a)
    const half_len = parseInt(arr.length / 2)
    let current_len = arr.length

    for (var i=0; i < frequency.length; i++){
        current_len -= frequency[i]
        if (current_len <= half_len) return i+1
    }
};