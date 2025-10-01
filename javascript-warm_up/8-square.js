#!/usr/bin/node
const size = process.argv[2];
if (isNaN(size) || size === undefined) {
    console.log("Missing size");
} else {
    const n = parseInt(size);
    for (let i = 0; i < n; i++) {
        let row = '';
        for (let j = 0; j < n; j++) {
            row += 'X';
        }
        console.log(row);
    }
}
