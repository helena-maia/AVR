# AVR
MOTION ESTIMATION USING LUCAS-KANADE 


create_direction.py: slightly modified version of [Adaptive Visual Rhythm](https://github.com/darwinTC/Adaptive-Visual-Rhythms-for-Action-Recognition.git)

Compute the predominant direction (1 = vertical, 2 = horizontal) for each class from src_dir or for a fixed class. The former generates the direction_dir/direction.txt file, whereas the latter generates the direction_dir/class_name.txt one.

python create_direction.py --src_dir <src_dir> --direction_dir <direction_dir> --ext <avi/mp4> --class_name <class_name>

Every class: python create_direction.py --src_dir videos/ --direction_dir direction/ --ext mp4

Single class: python create_direction.py --src_dir videos/ --direction_dir direction/ --ext mp4 --class_name abseiling

----

VISUAL RHYTHM COMPUTATION

pool_vr.py: Compute visual rhythm (mean) for each video from video_list located at video_dir. Resulting VR images are saved in vr_dest. Parallel version (--num_worker).

python pool_vr.py <video_dir> <video_list> <vr_dest> --num_worker <num_worker> --ext <avi/mp4>

python pool_vr.py videos/ video_list.txt vr/ --num_worker 4 --ext mp4

video_list.txt: list of file names. Ex: ls videos/ > video_list.txt

remove_empty_vr.py: Remove empty folders and 0-byte images.

python remove_empty_vr.py <vr_dir>

python remove_empty_vr.py vr/


missing_vr.py: List missing folders (videos).

python missing_vr.py <video_list> <vr_dir> <missing_list>

python missing_vr.py video_list.txt vr/ missing.txt










