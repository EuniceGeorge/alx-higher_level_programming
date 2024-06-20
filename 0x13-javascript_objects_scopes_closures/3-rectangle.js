#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
        return;
     
     this.width = w;
     this.height = h; 

     calcArea() {
	     return this.width * this.heigth;

     print() {
       
    }
  }
}
module.exports = Rectangle;
