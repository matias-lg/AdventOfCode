import { readFileSync } from "fs";

type DirNode = {
  dirname: string;
  childrenDir: { [dirname: string]: DirNode };
  files: { [filename: string]: number };
  parent?: DirNode;
};

const root: DirNode = {
  dirname: "\\",
  childrenDir: {},
  files: {},
};

let cwd = root;

const inp = readFileSync("./input", "utf8").split("\n").slice(1, -1);

const getTokens = (idx: number): string[] => inp[idx].split(" ");

let idx = 0;
while (idx < inp.length) {
  let tokens = getTokens(idx);
  // user input
  if (tokens[0] == "$") {
    switch (tokens[1]) {
      case "ls":
        idx++;
        while (idx < inp.length && getTokens(idx)[0] != "$") {
          let childTokens = getTokens(idx);
          if (childTokens[0] == "dir") {
            if (!cwd.childrenDir[childTokens[1]])
              cwd.childrenDir[childTokens[1]] = {
                parent: cwd,
                dirname: childTokens[1],
                childrenDir: {},
                files: {},
              };
          } else {
            if (!cwd.files[childTokens[1]])
              cwd.files[childTokens[1]] = parseInt(childTokens[0]);
          }
          idx++;
        }
        break;

      case "cd":
        let targetDir = tokens[2];
        if (targetDir == "..") {
          if (cwd.parent) cwd = cwd.parent;
        } else cwd = cwd.childrenDir[tokens[2]];
        idx++;
        break;

      default:
        console.error(`Unexpected keyword ${tokens[0]}`);
        idx++;
    }
  }
}

let AT_MOST = 100000;
let atMostSum = 0;

const getDirSizes = (dir: DirNode): number => {
  let totalSize = Object.values(dir.files).reduce((acc, x) => acc + x, 0);
  let childrens = Object.keys(dir.childrenDir);
  if (childrens.length > 0) {
    totalSize += childrens
      .map((child) => getDirSizes(dir.childrenDir[child]))
      .reduce((acc, v) => acc + v, 0);
  }
  if (totalSize <= AT_MOST) atMostSum += totalSize;
  console.log(dir.dirname, totalSize);
  return totalSize;
};

getDirSizes(root);
console.log(`at most ${AT_MOST}:`, atMostSum);
