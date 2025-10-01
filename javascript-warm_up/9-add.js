#!/usr/bin/node
const a = Number(process.argv[2])
const b = Number(process.argv[3])

function add(x, y) {
  return x + y
}

console.log(add(a, b))
