// Runtime 79 ms Beats 97.40%
// Memory 44.5 MB Beats 76.19%
/**
 * @param {number[]} g
 * @param {number[]} s
 * @return {number}
 */
var findContentChildren = function (g, s) {
  const sort = (array) => array.sort((a, b) => b - a); // 내림차순 정렬
  const [children, cookies] = [sort(g), sort(s)];

  let count = 0;

  children.forEach((child) => {
    // 제일 큰 쿠키부터 줄 수 있으면 주고 다음 쿠키, 줄 수 없으면 다음 어린이
    if (child <= cookies[count]) count += 1;
  });

  return count;
};
