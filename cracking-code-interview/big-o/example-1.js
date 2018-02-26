// The runtime will be O(n), the fact that it does run for twice won't matter, gets rid of constants
function sumAndProduct(array) {
  let sum = 0;
  let product = 1;
  for (let i in array) {
    sum += array[i];
  }
  for (let i in array) {
    product *= array[i];
  }
  console.log(`sum = ${sum}, product = ${product}`);
}

let array = [1, 5, 8, 9, 11, 13, 15, 19, 21];
sumAndProduct(array);
