import fs from "fs";

const rolls: string[][] = fs
  .readFileSync("day4_input.csv", "utf-8")
  .trim()
  .split("\n")
  .map((line: string) => line.split(""));

const width = rolls[0].length;
const height = rolls.length;

// PART ONE
function getNumAround(x: number, y: number): number {
  let count = 0;

  for (let dx = -1; dx <= 1; dx++) {
    for (let dy = -1; dy <= 1; dy++) {
      if (dx === 0 && dy === 0) continue; // skip self
      const nx = x + dx;
      if (nx < 0 || nx >= width) continue;
      const ny = y + dy;
      if (ny < 0 || ny >= height) continue;

      if (rolls[ny][nx] === "@") count++;
    }
  }

  return count;
}

let numAccessible = 0;
for (let y = 0; y < height; y++) {
  for (let x = 0; x < width; x++) {
    if (rolls[y][x] !== "@") continue;
    if (getNumAround(x, y) >= 4) continue;

    numAccessible++;
  }
}
console.log(`Number of accessible rolls (1): ${numAccessible}`);

// PART TWO
numAccessible = 0;
while (true) {
  let removed = [];
  for (let y = 0; y < height; y++) {
    for (let x = 0; x < width; x++) {
      if (rolls[y][x] !== "@") continue;
      if (getNumAround(x, y) >= 4) continue;

      removed.push([y, x]);
    }
  }

  if (removed.length === 0) break;

  numAccessible += removed.length;
  for (const [y, x] of removed) {
    rolls[y][x] = ".";
  }
}
console.log(`Number of accessible rolls (2): ${numAccessible}`);
