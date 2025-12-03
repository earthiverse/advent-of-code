import fs from "fs";

const ranges: [string, string][] = fs
  .readFileSync("day2_input.csv", "utf-8")
  .trim()
  .split(",")
  .map((range: string) => range.split("-"));

// PART ONE
let sum = 0;
for (const [start, end] of ranges) {
  for (let i = parseInt(start); i <= parseInt(end); i++) {
    const string = i.toString();
    let isRepeatingPattern: boolean = true;
    switch (string.length % 2) {
      case 0: {
        // even length
        const half = string.length / 2;
        for (let j = 0; j < half; j++) {
          if (string[j] !== string[half + j]) {
            isRepeatingPattern = false;
            break;
          }
        }
        break;
      }
      case 1: {
        isRepeatingPattern = false;
        break;
      }
    }
    if (isRepeatingPattern) {
      //   console.debug(`Repeating pattern found: ${string}`);
      sum += i;
    }
  }
}
// console.log(`Repeating pattern sum (1): ${sum}`);

// PART TWO
sum = 0;
for (const [start, end] of ranges) {
  for (let i = parseInt(start); i <= parseInt(end); i++) {
    const string = i.toString();
    let isRepeatingPattern: boolean = false;

    section: for (
      let sectionLength = 1;
      sectionLength <= string.length / 2;
      sectionLength++
    ) {
      if (string.length % sectionLength !== 0) {
        continue; // Not divisible by section length
      }
      //   console.debug(`Checking ${string} by ${sectionLength}...`);
      for (let j = 0; j < sectionLength; j++) {
        const charToMatch = string[j];
        for (let k = 1; k < string.length / sectionLength; k++) {
          const pos = j + k * sectionLength;
          if (string[pos] !== charToMatch) {
            // console.debug(
            //   `${string[pos]} does not match ${charToMatch} (${j}, ${pos})`
            // );
            continue section;
          }
        }
      }
      isRepeatingPattern = true;
      break;
    }
    if (isRepeatingPattern) {
      console.debug(`Repeating pattern found: ${string}`);
      sum += i;
    }
  }
}
console.log(`Repeating pattern sum (1): ${sum}`);
