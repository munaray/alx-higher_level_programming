#!/usr/bin/node
import SquareClass from "./5-square.js";

class Square extends SquareClass {
	charPrint(c) {
		if (c === undefined) {
			c = "X";
		}
		for (let i = 0; i < this.height; i++) {
			let s = "";
			for (let j = 0; j < this.width; j++) {
				s += c;
			}
			console.log(s);
		}
	}
}

module.exports = Square;
