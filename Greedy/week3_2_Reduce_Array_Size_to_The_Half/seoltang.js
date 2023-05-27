// time complexity = O(n log n)
// space complexity = O(n)
/**
 * @param {number[]} arr
 * @return {number}
 */
var minSetSize = function (arr) {
  const count = {};

  arr.forEach((num) => {
    count[num] = count[num] ? count[num] + 1 : 1;
  });

  let set = 0;
  let answer;

  Object.values(count)
    .sort((a, b) => b - a)
    .some((countNum, index) => {
      set += countNum;
      answer = index + 1;
      return set >= arr.length / 2;
    });

  return answer;
};
