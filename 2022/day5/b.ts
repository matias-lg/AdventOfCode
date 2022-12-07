import { readFileSync } from "fs";

const inp = readFileSync("./input", "utf8").split("\n").slice(0, -1);
// find number of stacks
let boxEnd = 0;
while (inp[boxEnd][1] != "1") boxEnd++;
let stacksPos = inp[boxEnd];
const stacks: string[][] = [];

for (let i = 0; i < stacksPos.split(" ").filter((x) => x != "").length; i++)
  stacks.push([]);

for (let j = 0; j < stacksPos.length; j++) {
  if (["", "\n", " "].includes(stacksPos[j])) continue;
  let sn = parseInt(stacksPos[j]) - 1;
  for (let i = 0; i < boxEnd; i++) {
    if (inp[i][j] != " ") {
      stacks[sn].push(inp[i][j]);
    }
  }
}

for (let arr of stacks) arr.reverse();

for (let i = boxEnd + 2; i < inp.length; i++) {
  let match = inp[i].match(/move ([0-9]+) from ([0-9]+) to ([0-9]+)/i);
  if (match) {
    let [q, from, to] = [match[1], match[2], match[3]].map((x) => parseInt(x));
    let to_push = [];
    while (q--) {
      to_push.push(stacks[from - 1].pop() as string);
    }
    to_push.reverse();
    stacks[to - 1].push(...to_push);
  }
}

let res = "";
for (let i = 0; i < stacks.length; i++) {
  if (stacks[i].length > 0) res += stacks[i].pop();
}
console.log(res);
