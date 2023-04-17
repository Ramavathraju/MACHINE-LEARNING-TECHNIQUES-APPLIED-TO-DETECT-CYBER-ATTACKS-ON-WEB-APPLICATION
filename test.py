









import re
import Needleman




def main():
   strs = ""
   with open("normalTrafficTraining.txt", "r") as file:
    for line in file:
      line = line.strip('\n')
      x = re.findall("[a-z]+[:.].*?(?=\s)", line)
      strs = strs.join(x)
      if strs.startswith("http"):
        value  = Needleman.needle(strs,"kaleem")
        print(strs+" "+str(value))   

if __name__ == '__main__':
    main()