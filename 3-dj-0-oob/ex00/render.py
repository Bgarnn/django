import sys, os, settings

def render(file_name):
    try:
        name_split = (os.path.splitext(file_name)) #os.path.splitext() return tuple of 1.root 2.extension
        if name_split[1] != ".template":
            print("wrong file extension")
            sys.exit(1)
        with open(file_name, 'r') as infile:
            outfile_name = name_split[0] + ".html"
            outfile = open(outfile_name, "w")
            for line in infile:
                line_new = (line.replace("{name}", settings.name)
                                .replace("{firstname}", settings.firstname)
                                .replace("{lastname}", settings.lastname)
                                .replace("{age}", settings.age)
                                .replace("{profession}", settings.profession))
                outfile.write(line_new)
            outfile.close()
    except FileNotFoundError:
        print("File not found") 
        sys.exit(1)
if __name__ == '__main__':
    if len(sys.argv) == 2:
        render(sys.argv[1])
    else:
        print("wrong number of arguments")
        sys.exit(1)