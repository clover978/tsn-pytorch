import os
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, Executor

video_path = '/home/dxx/UCF101/UCF101/'
frame_path = '/home/dxx/UCF101/UCF101_frm/'
def extract_job(video):
    in_name = os.path.join(video_path, video)
    out_name = os.path.join(frame_path, video[:video.lfind('.')])
    if not os.path.exists(out_name):
        os.makedirs(out_name)
        # extract every 4 frames
        cmd = 'ffmpeg -loglevel panic -i {} -vf "select=not(mod(n\,4))" -vsync vfr -q 0 {}/img_%05d.jpg'.format(in_name, out_name)
        ## print(cmd)
        os.system(cmd)
    print(video)
    ## os.remove(video)

if __name__ == '__main__':
    video_list = [ x.strip() for x in open('trainvallist.txt').readlines() ]
    with ThreadPoolExecutor(max_workers=10) as pool:
        pool.map(extract_job, video_list)

