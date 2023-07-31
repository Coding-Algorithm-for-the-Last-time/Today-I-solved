// Runtime 363 ms Beats 70.45%
// Memory 56.5 MB Beats 91.67%
/**
 * @param {number[]} nums
 * @return {number}
 */
var minPairSum = function (nums) {
  const sortedNums = nums.sort((a, b) => a - b);

  // 가우스 등차수열의 합 구할 때처럼 양 끝에서부터 짝지어서 더함
  return sortedNums.reduce((acc, cur, index) => {
    const sum = cur + sortedNums[sortedNums.length - index - 1];
    return sum > acc ? sum : acc;
  });
};
