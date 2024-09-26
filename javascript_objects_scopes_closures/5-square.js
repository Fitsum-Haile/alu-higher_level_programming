// 5-square.js
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size); // Call the parent constructor with width and height both as size
  }
}

module.exports = Square;
