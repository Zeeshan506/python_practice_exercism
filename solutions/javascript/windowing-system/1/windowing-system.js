// @ts-check

/**
 * Implement the classes etc. that are needed to solve the
 * exercise in this file. Do not forget to export the entities
 * you defined so they are available for the tests.
 */

export function Size (width,height)
{
  this.width = (width ?? 80);
  this.height = (height ?? 60);
}

Size.prototype.resize = function (w,h){
  this.width = w;
  this.height = h;
}
   
export function Position (x,y){
  this.x = (x ?? 0);
  this.y = (y ?? 0);
}

Position.prototype.move = function (newX, newY){
  this.x = newX;
  this.y  = newY;
}

export class ProgramWindow{
  constructor(width,height){
    this.screenSize = new Size(width ?? 800,height ?? 600);
    this.size = new Size();
    this.position = new Position();
  }

resize(paramSize) {
    let minWidth = Math.max(1,paramSize.width);
    let minHeight = Math.max(1,paramSize.height);

    const maxWidth = this.screenSize.width - this.position.x;
    const maxHeight = this.screenSize.height - this.position.y;

    minWidth = Math.min(maxWidth,minWidth);
    minHeight = Math.min(maxHeight,minHeight);
  this.size = new Size(minWidth,minHeight);
}

move(paramPos){
 let newX = Math.max(0, paramPos.x); 
  let maxX = this.screenSize.width - this.size.width;
  newX = Math.min(newX, maxX);

  let newY = Math.max(0, paramPos.y);
  let maxY = this.screenSize.height - this.size.height;
  newY = Math.min(newY, maxY);

  this.position = new Position(newX, newY);
}
}

export function changeWindow(ProgramWindow){
 ProgramWindow.resize(new Size(400,300));
 ProgramWindow.move(new Position(100,150)); 
  return ProgramWindow;
}