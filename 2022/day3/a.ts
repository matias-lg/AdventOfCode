import { readFileSync } from "fs";

const alphabet = "abcdefghijklmnopqrstuvwxyz";

const lines = readFileSync("./input", "utf8").split("\n").slice(0, -1);

let priorities: string[] = [];
let result = 0;

for (let line of lines) {
  let left = new Set<string>();
  let right = new Set<string>();
  let count = 0;
  for (let char of line.split("")) {
    if (count < line.length / 2) left.add(char);
    else right.add(char);
    count++;
  }
  priorities.push(Array.from(left).filter((x) => right.has(x))[0]);
}

for (let p of priorities) {
  if (p == p.toUpperCase()) result += 26;
  result += alphabet.indexOf(p.toLowerCase()) + 1;
}

console.log(result);
