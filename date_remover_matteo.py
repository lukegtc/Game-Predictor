import ast

def date_remover(filename):
    fin = open(filename)
    fout = open(filename + "no_date", "w+")
    for line in fin:
        line = ast.literal_eval(line)
        line = line[:-1]
        fout.write(str(line) + "\n")


date_remover("season20092010.txt")
date_remover("season20102011.txt")
date_remover("season20112012.txt")
date_remover("season20132014.txt")
date_remover("season20142015.txt")
date_remover("season20152016.txt")
date_remover("season20162017.txt")
date_remover("season20172018.txt")
date_remover("season20182019.txt")