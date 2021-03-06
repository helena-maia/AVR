from multiprocessing import Pool
import cv2
import numpy as np
import os
import argparse
import glob

def run_vr(x):
    ind = x[0]
    video_path = x[1][0]
    dest = x[1][1]

    video_name = video_path.split("/")[-1]
    vr_dest = os.path.join(dest,video_name[:-4])

    if (os.path.isdir(vr_dest)): 
        print (vr_dest, " folder already exists")
        return 

    cap = cv2.VideoCapture(video_path)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)   # float
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # float

    hor_vr = np.array([]).reshape(0,int(width),3)
    ver_vr = np.array([]).reshape(0,int(height),3)

    while(cap.isOpened()):
        ret, img = cap.read()

        if ret == True:
            hor = np.mean(img, axis=0)
            ver = np.mean(img, axis=1)
    
            hor_vr = np.vstack([hor_vr,[hor]])
            ver_vr = np.vstack([ver_vr,[ver]])
        else:
            break

    if hor_vr.size == 0 or ver_vr.size == 0: 
        print("Error opening video file ", video_name)
        return

    hor_vr = np.swapaxes(hor_vr, 0,1)
    ver_vr = np.swapaxes(ver_vr, 0,1)
    
    print("creating folder: "+vr_dest)
    os.makedirs(vr_dest)

    cv2.imwrite(os.path.join(vr_dest,"hor_vr.jpg"), hor_vr)
    cv2.imwrite(os.path.join(vr_dest,"ver_vr.jpg"), ver_vr)

def getArgs():
    parser = argparse.ArgumentParser(description='Compute visual rhythm (mean).')
    parser.add_argument("video_dir", action='store', type=str, help="directory that contains the subclips")
    parser.add_argument("video_list", action='store', type=str, help="list of subclips (without path)")
    parser.add_argument("vr_dest", action='store', type=str, help="directory to save the visual rhythm images")
    parser.add_argument('--num_worker', type=int, default=8, help='')
    parser.add_argument('--ext', type=str, default='avi', choices=['avi','mp4'], help='video file extensions')
    return parser.parse_args()

if __name__ == "__main__":
    args = getArgs()

    num_worker=args.num_worker
    vr_dest = args.vr_dest
    videos = np.loadtxt(args.video_list, dtype='U100')
    videos = [ os.path.join(args.video_dir,v) for v in videos ]


    if not os.path.isdir(vr_dest):
        print("creating folder: "+vr_dest)
        os.makedirs(vr_dest)

    pool = Pool(num_worker)
    pool.map(run_vr,enumerate(zip(videos, len(videos)*[vr_dest])))
