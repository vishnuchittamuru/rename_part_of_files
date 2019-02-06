import os

def main():

    for filename in os.listdir("."):
        if ".txt" not in filename:
            continue
        else:
            x = filename.split('-')
            if len(x) > 1:
                y = 'replaced'
                os.rename(filename, x[0] + y + x[1])

main()
