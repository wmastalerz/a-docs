# execute after remove unneeded :alt:
import os
import re

rstname = os.path.join("index.rst")
print(rstname)

def icon_register(lines):
    """
    Register Icone before usadge of it.
    """
    icon_name=""
    pic_name=""
    output_lines = []
    for line in lines:
        if "(|D:\\" in line:
            output_lines.append(".. |"+icon_name+"| image::"+pic_name+"\n   :height: 25px\n") 
        output_lines.append(line)
    return output_lines

def icon_rename(input_string):
    """
    Cleanup Icone name.
    """
    output_string = re.sub(r'D:\\(.*)\\\\', '', input_string,0, re.MULTILINE)
    return output_string

if __name__ == "__main__":        
    with open(rstname, "r") as input_file:
        lines = input_file.readlines()

    result1=icon_register(lines)
    final=icon_rename(result1)

    with open("output.rst", "w") as output_file:
        output_file.writelines(final)
