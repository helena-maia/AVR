import os
import numpy as np
import argparse

def getArgs():
    parser = argparse.ArgumentParser(description='Download dataset.')
    parser.add_argument("video_list", action='store', type=str, help="path to the list of subclips")
    parser.add_argument("vr_dir", action='store', type=str, help="directory with the visual rhythm images")
    parser.add_argument("missing_list", action='store', type=str, help="path to the output")
    return parser.parse_args()



if __name__ == "__main__":
    args = getArgs()

    video_list = np.loadtxt(args.video_list,dtype='U100')
    
    missing = []

    for i,v in enumerate(video_list):
        print ("%d of %d"%(i,len(video_list)))

        if not os.path.isdir(os.path.join(args.vr_dir, v[:-4])): 
            print (os.path.join(args.vr_dir, v[:-4]))
            print (v)
            missing.append(v)

    np.savetxt(args.missing_list, missing, fmt="%s")
