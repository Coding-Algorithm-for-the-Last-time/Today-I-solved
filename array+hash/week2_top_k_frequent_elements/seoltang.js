/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  const groups = [];

  nums.forEach((num) => {
    const index = groups.findIndex((group) => group.includes(num));

    if (index === -1) groups.push([num]);
    else groups[index].push(num);
  });

  return groups
    .sort((a, b) => b.length - a.length)
    .slice(0, k)
    .map((group) => group[0]);
};
