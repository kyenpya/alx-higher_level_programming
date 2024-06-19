#!/usr/bin/node

function callMeMo (x, theFunction) {
  if (x > 0) {
    theFunction();
    callMeMo(x - 1, theFunction);
  }
}

module.exports.callMeMo = callMeMo;
