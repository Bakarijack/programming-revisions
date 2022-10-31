//var docxConverter = require('docx-pdf');
import docxConverter from 'docx-pdf';

docxConverter('./sub.docx','./sub.pdf',function(err,result){
  if(err){
    console.log(err);
  }
  console.log('result'+result);
});
/*

docxConverter(inputPath,outPath,function(err,result){
  if(err){
    console.log(err);
  }
  console.log('result'+result);
});
*/