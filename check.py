import os

# -178|2:58|PT|Flying not allowed|FlyingNotAllowed.wav|0|0|False

#Global directory for audio files
BASEDIR = "./Audio/"


# parse through all *.timer files in the directory and call processFile on each one
def check():
    for file in os.listdir("."):
        if file.endswith(".timer"):
            print("Processing " + file)
            processFile(file)

def checkWavFileExists(fileName):
    # check if the file exists
    if not os.path.isfile(BASEDIR + fileName):
        print("File does not exist: " + fileName)
        return False



def processLine(line):
            # split the line into its components
            components = line.split("|")
            
            # check if the line is valid
            if len(components) != 8:
                print("Invalid line: " + line)
                return
            # if #4 is not empty, take #5 and #6
            if components[4] == "":
                print("Beep: " + components[5]+ " " + components[6])
                return
            else:  checkWavFileExists(components[4])


def processFile(file):
    with open(file, "r") as f:
        f.readline()
        lines = f.readlines()
        for line in lines:
            processLine(line)


check()