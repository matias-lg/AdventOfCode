import { readFileSync } from "fs";

const alphabet = "abcdefghijklmnopqrstuvwxyz";
const complete = alphabet + alphabet.toUpperCase();

const lines = readFileSync("./input", "utf8").split("\n").slice(0, -1);

let threes: string[][] = [];
let result = 0;

let i = 0;
while (i < lines.length) {
  let arr = [];
  let cnt = 0;
  while (cnt < 3) {
    arr.push(lines[i]);
    cnt++;
    i++;
  }
  threes.push(arr);
}

for (let t of threes) {
  let freqs = [{}, {}, {}];
  for (let char of complete) for (let i = 0; i < 3; i++) freqs[i][char] = 0;
  for (let i = 0; i < 3; i++) for (let char of t[i]) freqs[i][char]++;
  for (let char of complete) {
    if (Math.min(freqs[0][char], freqs[1][char], freqs[2][char]) > 0) {
      if (char == char.toUpperCase()) result += 26;
      result += alphabet.indexOf(char.toLowerCase()) + 1;
      break;
    }
  }
}
console.log(result);
