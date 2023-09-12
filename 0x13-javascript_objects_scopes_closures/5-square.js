#!/usr/bin/node
import Rectangle from "./4-rectangle.js";

class Square extends Rectangle {
	constructor(size) {
		super(size, size);
	}
}

export default Square;
