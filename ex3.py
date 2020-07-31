import sys
import os

if os.path.exists("src.txt") :
    print(sys.argv)
    fr = open("src.txt", "r") # open(sys.argv[1], "r")
    fw = open("dst.txt", "w") # open(sys.argv[2], "r")

    for line in fr:
        fw.write(line)
        
    fr.close()
    fw.close()
else:
    print("파일이 존재하지 않는다")