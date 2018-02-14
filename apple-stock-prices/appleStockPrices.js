let stockPricesYesterday = [10, 7, 5, 8, 11, 9];
// stockPricesYesterday = [12,13,5,6,17,20,19,15,30]
// stockPricesYesterday = [12,5,15,4,5,6,7,1,13]
// stockPricesYesterday = [15,14,13,10,9,8,3,10,13,20]
stockPricesYesterday = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6];
const getMaxProfit = list => {
  let smallest = list[0];
  let biggest = list[0];

  list.forEach(el => {
    if (el < smallest) {
      smallest = el;
      biggest = el;
    } else {
      if (el > biggest) {
        biggest = el;
      }
    }
  });
  return biggest - smallest;
};

console.log(getMaxProfit(stockPricesYesterday));
