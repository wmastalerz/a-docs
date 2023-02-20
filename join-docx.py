# Script joining the docx files into one.
######### example: python join-docx.py  output.docx input1-base.docx input2.docx input3.docx

import docx
import sys
import logging

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger('join-docx')


def join_doc():
    """
    Join an .docx files into one file.
    """
    
    try:    
        file1_path = sys.argv[2] 
        doc1=docx.Document(file1_path)
        print("base:"+file1_path)

        for arg in sys.argv[3:]:
            file_path = arg
            print("...adding: "+file_path)    
            # load file into Document objects
            doc = docx.Document(file_path)
            # append the content of doc to doc1
            for element in doc.element.body:
                doc1.element.body.append(element)
            
        # specify and save the output file
        output_path = sys.argv[1]
        doc1.save(output_path)
        print("output: "+output_path)
    except (docx.opc.exceptions.PackageNotFoundError) as e:
        logger.error(str(e).replace("Package", " File"))
    except (IndexError) as e:
        logger.error(str(e).replace("list index out of range", " Use: \"python join-docx.py  output.docx input1-base.docx input2.docx ...\""))
                
join_doc()
