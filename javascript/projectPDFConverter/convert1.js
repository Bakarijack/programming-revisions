// In EcmaScript 5...
 
import nodePandoc from 'node-pandoc';
var src, args, callback;
 
src = './sub.docx';
 
// Arguments can be either a single string:
args = '-f docx -t markdown -o ./markdown.md';
// Or in an array of strings -- careful no spaces are present:
args = ['-f','docx','-t','markdown','-o','markdown.md'];
 
// Set your callback function
callback = function (err, result) {
 
  if (err) {
    console.error('Oh Nos: ',err);
  }
 
  // For output to files, the 'result' will be a boolean 'true'.
  // Otherwise, the converted value will be returned.
  console.log(result);
  return result;
};
 
// Call pandoc
nodePandoc(src, args, callback);