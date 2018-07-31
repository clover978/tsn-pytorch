import os

in_file = 'trainlist.txt'
out_file = 'train_tsn.lst'

with open('classInd.txt') as f: 
    d = { klass:ind for klass, ind in f.readlines().strip().split() }
print(d)
 
frame_path = '/home/dxx/UCF101/UCF101_frm/'
with open(out_file, 'w') as f:
    for line in open(in_file):
        video = line.split()[0]
        image_dir = os.path.join( frame_path, video[:video.lfind('.')] )

        frm_cnt = len(os.listdir(image_dir))

        label = video.split('/')[1]
        ind = d[label]

        f.write( '{} {} {}\n'.format(image_dir, frm_cnt, ind) )
