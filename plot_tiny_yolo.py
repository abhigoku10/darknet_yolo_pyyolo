######################################
# Plotting of the learning rate for tiny_yolo  
######################################

###python plot_tiny_yolo.py C:\darknet\build\darknet\x64\temp.log 0

import argparse 
import sys
import matplotlib.pyplot as plt


def main(argv):

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "log_file",
        help = "path to log file"
        )


    parser.add_argument(
        "option",
        help = "0 -> loss vs iter"
        )
    
    args = parser.parse_args()


    f = open(args.log_file)
    
    lines  = [line.rstrip("\n") for line in f.readlines()]
    
    # skip the first 3 lines
    lines = lines[3:]
    
    numbers = {'1','2','3','4','5','6','7','8','9','0'}


    iters = []
    loss = []
    for line in lines:
		
        if line[0] in numbers:

            args = line.split(" ")
            args_length = len(args)
            if (args_length ==1):continue
            if (float(args[2]) == 'nan'):continue
            print(len(args))
            print(int(args[0][:-1]))
            print(float(args[2]))
            iters.append(int(args[0][:-1]))            
            loss.append(float(args[2]))  
            
    #plt.plot(iters[:40000],loss[:40000])
    plt.plot(iters,loss)
    plt.xlabel('iters')
    plt.ylabel('loss')
    plt.grid()


    plt.show()
    
if __name__ == "__main__":
    main(sys.argv)