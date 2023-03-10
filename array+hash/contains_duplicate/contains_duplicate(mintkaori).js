/**
 * @param {number[]} nums
 * @return {boolean}
 */
const containsDuplicate = function(nums) {
    if(new Set(nums).size != nums.length){return true;} else {return false};
};
