#!usr/bin/node
const x = process.argv[2];
const count = parseInt(x);

if (isNaN(count)) {
    console.log('Missing number of occurrences');
} else {
    let i = 0;
    while (i < count) {
        console.log('C is fun');
        i++;
    }
}
