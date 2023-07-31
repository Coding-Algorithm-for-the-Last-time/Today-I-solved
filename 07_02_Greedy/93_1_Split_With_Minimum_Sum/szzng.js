// Runtime 56 ms Beats 73.46%
// Memory 41.3 MB Beats 98.53%

var splitNum = function (num) {
    num = String(num).split('').sort()
    let a = ''
    let b = ''

    for (var i = 0; i < num.length; i += 2) a += num[i]
    for (i = 1; i < num.length; i += 2) b += num[i]

    return Number(a) + Number(b)
};