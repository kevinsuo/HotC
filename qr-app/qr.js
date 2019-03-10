/*
 * $ nodejs qr.js
 */


var qr = require('qr-image');
var fs = require('fs');

var code = qr.image('http://www.google.com', { type: 'svg' });
var output = fs.createWriteStream('output.svg')

code.pipe(output);
