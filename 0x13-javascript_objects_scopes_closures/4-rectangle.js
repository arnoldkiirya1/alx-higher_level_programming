#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0) {
      // If width or height is not positive, create an empty object
      return {};
    }
    this.width = w;
    this.height = h;
  }

  print() {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate() {
    [this.width, this.height] = [this.height, this.width]; // Swap width and height
  }

  double() {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
