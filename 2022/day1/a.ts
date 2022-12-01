// read content from file input_a.txt
import { readFileSync } from "fs";
const inputFile = readFileSync("./input_a.txt", "utf8");
const calories = inputFile.split("\n").map((x) => parseInt(x));

let [max, acc] = [-1, 0];
for (let cal of calories) {
  if (isNaN(cal)) {
    max = Math.max(max, acc);
    acc = 0;
  } else {
    acc += cal;
  }
}

console.log(max);
