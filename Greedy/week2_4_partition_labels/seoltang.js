// Runtime 65 ms Beats 83.57%
// Memory 42.6 MB Beats 93.33%
/**
 * @param {string} s
 * @return {number[]}
 */
var partitionLabels = function (s) {
  const size = [];
  let [left, right] = [-1, 0]; // 파티션 왼쪽, 오른쪽

  for (let index = 0; index < s.length; index++) {
    const lastIndex = s.lastIndexOf(s[index]);

    if (right < lastIndex) right = lastIndex; // 파티션 오른쪽으로 최대한 늘리기

    // 파티션 오른쪽에 도달하면
    if (index === right) {
      size.push(right - left); // 파티션 사이즈 저장
      left = right; // 파티션 왼쪽도 오른쪽에 맞추기
    }
  }

  return size;
};
