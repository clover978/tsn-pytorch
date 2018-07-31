:<<!
# Train
CUDA_VISIBLE_DEVICES=0,1,2,3 \
        python -u ../main.py ucf101 RGB train_tsn.txt val_tsn.txt \
        --arch BNInception \
	--num_segments 5 --gd 20 --lr 0.001 --lr_steps 70 130 --epochs 180 \
	-b 140 -j 8 --dropout 0.5 --snapshot_pref meitu_bninception |& tee log.txt
!

:<<!
# Resume
CUDA_VISIBLE_DEVICES=0,1,2,3 \
        python -u ../main.py ucf101 RGB train_tsn.txt val_tsn.txt \
        --arch BNInception \
        --resume models/meitu_bninception_rgb_1_checkpoint.pth.tar \
        --num_segments 5 --gd 20 --lr 0.001 --lr_steps 70 130 --epochs 180 \
        -b 140 -j 8 --dropout 0.5 --snapshot_pref meitu_bninception |& tee log.txt
!

:<<!
# Test
CUDA_VISIBLE_DEVICES=0 \
       python ../test_models.py ucf101 RGB /home/lk/pytorch/TSN/val.txt ucf101_bninception_rgb_checkpoint.pth.tar \
       --arch BNInception \
       --save_scores ./rgb_score.txt
!
