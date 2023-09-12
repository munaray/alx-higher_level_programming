#!/usr/bin/node
const dict = require("./101-data").dict;

const listSum = Object.entries(dict);
const value = Object.values(dict);
const uniqueValue = [...new Set(value)];
const newDict = {};
for (const j in uniqueValue) {
	const list = [];
	for (const k in listSum) {
		if (listSum[k][1] === uniqueValue[j]) {
			list.unshift(listSum[k][0]);
		}
	}
	newDict[uniqueValue[j]] = list;
}
console.log(newDict);
