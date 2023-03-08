# execute after remove unneeded :alt:
import os
rstname = os.path.join(os.path.realpath, os.argv[1],"index.rst")

def icon_register(input_name, pic_name,icon_name):
    """
    Register Icone before usadge of it.
    """
    with open(input_name, "r") as input_file:
        lines = input_file.readlines()
    output_lines = []
    for line in lines:
        if "D:\\" in line:
            output_lines.append(".. |"+ icon_name +_"| image::" + pic_name +"\n   :height: 25px\n")  # add new line before "image"
        output_lines.append(line)
    with open("output.rst", "w") as output_file:
        output_file.writelines(output_lines)

if __name__ == "__main__":        
    icon_register(rstname, "003.png", "003")