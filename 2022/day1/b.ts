// read content from file input_a.txt
import { readFileSync } from "fs";
const inputFile = readFileSync("./input_a.txt", "utf8");
const calories = inputFile.split("\n").map((x) => parseInt(x));
let acc = 0;
let top3 = [-1, -2, -3];
for (let cal of calories) {
  if (isNaN(cal)) {
    for (let i = 0; i < 3; i++) {
      if (top3[i] <= acc) {
        for (let j = 2; j > i; j--) {
          top3[j] = top3[j - 1];
        }
        top3[i] = acc;
        break;
      }
    }
    acc = 0;
  } else {
    acc += cal;
  }
}

console.log(
  top3,
  top3.reduce((a, b) => a + b, 0)
);
