/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var largestMerge = function (word1, word2) {
  let [i, j] = [0, 0];
  let merge = '';

  while (i < word1.length && j < word2.length) {
    if (word1.slice(i) > word2.slice(j)) {
      merge += word1[i];
      i += 1;
    } else {
      merge += word2[j];
      j += 1;
    }
  }

  merge += word1.slice(i) + word2.slice(j);
  return merge;
};
