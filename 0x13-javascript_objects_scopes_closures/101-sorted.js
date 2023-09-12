#!/usr/bin/node
const dictionary = require("./101-data").dictionary;

const listSum = Object.entries(dictionary);
const value = Object.values(dictionary);
const uniqueValue = [...new Set(value)];
const newDictionary = {};
for (const j in uniqueValue) {
	const list = [];
	for (const k in listSum) {
		if (listSum[k][1] === uniqueValue[j]) {
			list.unshift(listSum[k][0]);
		}
	}
	newDictionary[uniqueValue[j]] = list;
}
console.log(newDictionary);
