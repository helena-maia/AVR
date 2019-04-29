import os
import argparse
import shutil

def getArgs():
    parser = argparse.ArgumentParser(description='Remove empty folders and 0-byte images')
    parser.add_argument("vr_dir", action='store', type=str, help="directory with visual rhythm images")
    return parser.parse_args()

args = getArgs()

video_dir = os.listdir(args.vr_dir)

for v in video_dir:
    path = os.path.join(args.vr_dir, v)
    
    vr_images = os.listdir(path)
    total = len(vr_images)

    if(total == 0):
        os.rmdir(path)
        print("Empty: ",path)
    else:
        for i in vr_images:
            img_path = os.path.join(path,i)

            if os.stat(img_path).st_size == 0: 
                shutil.rmtree(path)
                print ("0-byte image",img_path)
                break
                
    
