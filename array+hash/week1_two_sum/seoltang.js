/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  const indices = [];

  nums.some((num, index) => {
    const complementIndex = nums.indexOf(target - num);
    if (complementIndex !== -1 && complementIndex !== index) {
      indices.push(index, complementIndex);
    }

    if (indices.length === 2) return true; // break
  });

  return indices;
};
