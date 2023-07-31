/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  const numsMap = new Map();

  nums.forEach((num) => {
    numsMap.set(num, (numsMap.get(num) | 0) + 1);
  });

  // 배열로 변경
  const countedNums = [];
  for ([key, value] of numsMap) {
    countedNums.push({ key, value });
  }

  // 많이 등장한 순서대로 정렬
  countedNums.sort((a, b) => b['value'] - a['value']);

  return countedNums.slice(0, k).map((item) => item.key);
};
