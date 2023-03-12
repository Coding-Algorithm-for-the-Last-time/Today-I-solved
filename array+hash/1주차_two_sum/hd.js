/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  for (let i = 0; i < nums.length; i++) {
    const idx = nums.indexOf(target - nums[i], i + 1);
    if (idx !== -1) return [i, idx];
  }
};
