import { join } from 'path';
import xtend from 'xtend';
import convert from 'ebook-convert';
 
// see more options at https://manual.calibre-ebook.com/generated/en/ebook-convert.html
var options = {
  input: join(__dirname, 'sample1.epub'),
  output: join(__dirname, 'example.pdf'),
  authors: '"Seth Vincent"',
  pageBreaksBefore: '//h:h1',
  chapter: '//h:h1',
  insertBlankLine: true,
  insertBlankLineSize: '1',
  lineHeight: '12',
  marginTop: '50',
  marginRight: '50',
  marginBottom: '50',
  marginLeft: '50'
};
 
/*
* create epub file
*/
convert(options, function (err) {
  if (err) console.log(err);
});