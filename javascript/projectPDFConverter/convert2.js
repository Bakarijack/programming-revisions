import getPageCount from 'docx-pdf-pagecount';

getPageCount('E:/sample/document/aa/sub.docx')
  .then(pages => {
    console.log(pages);
  })
  .catch((err) => {
    console.log(err);
  });
  