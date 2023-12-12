#!/usr/bin/node

const dict = require('./101-data').dict;
const new_dict = {};
for (key in dict)
{
  if (dict[key] in new_dict) {
    new_dict[dict[key]].push(key);
  } else {
    new_dict[dict[key]] = [key];
  }
}
console.log(new_dict);
