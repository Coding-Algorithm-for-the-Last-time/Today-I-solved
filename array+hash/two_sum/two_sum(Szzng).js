/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    while(nums.length >0){
        const lastIndex = nums.length-1
        const j = target - nums.pop()
        if (nums.includes(j)) return [nums.indexOf(j), lastIndex]
    }
};