/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  let [left, right] = [0, height.length - 1];
  let area = 0;

  while (left < right) {
    const [h, w] = [Math.min(height[left], height[right]), right - left];
    area = Math.max(area, h * w);
    height[left] < height[right] ? left++ : right--;
  }

  return area;
};
