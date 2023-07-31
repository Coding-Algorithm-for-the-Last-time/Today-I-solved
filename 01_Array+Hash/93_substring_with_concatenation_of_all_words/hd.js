const separateString = (string, length) => {
  let array = [];
  let str = '';

  string.split('').forEach((item, idx) => {
    if (str.length < length) {
      str += item;
    } else {
      array.push(str);
      str = item;
    }
    if (string.length === idx + 1) array.push(str);
  });

  return array;
};

/**
 * @param {string} s
 * @param {string[]} words
 * @return {number[]}
 */
var findSubstring = function (s, words) {
  let wordLength = words[0].length;
  let wordsLength = words.join('').length;

  const wordsMap = new Map();
  words.forEach((word) => {
    wordsMap.set(word, (wordsMap.get(word) || 0) + 1);
  });

  let answer = [];

  let pointer = 0;
  while (pointer < s.length - wordsLength + 1) {
    const concatString = separateString(
      s.slice(pointer, pointer + wordsLength),
      wordLength
    );

    const wordsMap = new Map();
    words.forEach((word) => {
      wordsMap.set(word, (wordsMap.get(word) || 0) + 1);
    });

    concatString.forEach((word) => {
      wordsMap.set(word, (wordsMap.get(word) || 0) - 1);
    });

    let isIncludes = [...wordsMap.values()].every((item) => item === 0);

    if (isIncludes) answer.push(pointer);

    pointer += 1;
  }

  return answer;
};
