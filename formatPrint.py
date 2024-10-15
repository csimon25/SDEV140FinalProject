# file name = formatPrint
# Author = Chad Simon
# Date = 5/15/22
# Summary = Format dollar amount

def formatPesos(inPesos):
    return "Chilean$" + format(inPesos, '.2f')

def formatEuros(inEuros):
    return "\u20ac" + format(inEuros, '.2f')
