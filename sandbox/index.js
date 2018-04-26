let string = 'We are the so-called "Vikings" from the north.';
let word = "a";
let x = removeWord(string, word);
let y = removeWord2(string, word);
console.log("x=", x, " y=", y, " = ", x === y);
let pallindrome = "?a man a plan a canal panama ";
console.log(pallindrome, isPallindrome(pallindrome));
console.log(pallindrome, isPallindrome2(pallindrome));
console.log(Number.MAX_VALUE);
const ChangeFontSize = id => {
  let name = "John";
  console.log("name", name.blink());
  document.getElementById(id).innerHTML = name.blink();
};

function removeWord(string, word) {
  let index = string.indexOf(word);
  if (index != -1) {
    var strippedWord =
      string.slice(0, index) +
      removeWord(string.slice(index + word.length), word);
  } else {
    return string;
  }
  return strippedWord;
}

function removeWord2(string, word) {
  return string.split(word).join("");
}

function isPallindrome(word) {
  // debugger;
  let reversed = word
    .split(" ")
    .join("")
    .split("")
    .reverse();
  console.log("is pallindrome", word, reversed.join(""));
  return (
    word ===
    word
      .split("")
      .reverse()
      .join("")
  );
}
function isPallindrome2(phrase) {
  let stripped = phrase.replace(/ /g, "");
  return (
    stripped ===
    stripped
      .split("")
      .reverse()
      .join("")
  );
}
