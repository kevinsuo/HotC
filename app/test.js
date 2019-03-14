/*
 * $ nodejs test.js
 *
 * alpine linux: apk add --update nodejs
 * then: node test.js
 */

var j=0;
for (i = 0; i < 10000000; i++ ) {
   j=j+i
}

console.log(j);


