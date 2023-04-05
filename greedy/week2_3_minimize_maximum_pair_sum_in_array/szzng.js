// Runtime 348 ms Beats 97.37%
// Memory 56.2 MB Beats 98.3%

var minPairSum = function(nums) {
    nums.sort((a,b)=>a-b)
    const numLength = nums.length
    const halfLength = numLength/2
    var maxSum = 0

    for (var i=0; i<halfLength; i++)
        maxSum = Math.max(nums[i] + nums[numLength-1-i] , maxSum)
    return maxSum
};