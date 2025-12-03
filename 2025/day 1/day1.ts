import fs from "fs";

const input: string[] = fs
  .readFileSync("day1_input.csv", "utf-8")
  .trim()
  .split("\n");

// PART ONE
let dial = 50;
let numZero = 0;
for (const line of input) {
  const direction = line[0] as "L" | "R";
  const distance = parseInt(line.substring(1));

  switch (direction) {
    case "L":
      dial -= distance;
      break;
    case "R":
      dial += distance;
      break;
  }
  while (dial < 0) dial = 100 + dial;
  while (dial >= 100) dial = dial - 100;
  if (dial === 0) numZero++;
  console.log(`Dial: ${dial}`);
}
console.log(`Num zeros (1): ${numZero}`);

// PART TWO
dial = 50;
numZero = 0;
for (const line of input) {
  const direction = line[0] as "L" | "R";
  const distance = parseInt(line.substring(1));

  let startingZero = dial === 0;

  switch (direction) {
    case "L":
      dial -= distance;
      break;
    case "R":
      dial += distance;
      break;
  }

  while (dial < 0) {
    dial = 100 + dial;
    if (startingZero) {
      startingZero = false;
      continue;
    }
    numZero++;
  }
  if (dial === 0) numZero++;
  while (dial >= 100) {
    dial = dial - 100;
    numZero++;
  }
  console.log(`Command: ${line} -> Dial: ${dial} -> Num zeros: ${numZero}`);
}
console.log(`Num zeros (2): ${numZero}`);
