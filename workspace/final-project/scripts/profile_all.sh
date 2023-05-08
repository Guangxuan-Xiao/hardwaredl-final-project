DESIGNS="eyeriss_like simba_like simple_output_stationary simple_weight_stationary"
NETS="alexent resnet18 resnet50 vgg11 vgg16 densenet121"

for design in $DESIGNS; do
    for net in $NETS; do
        echo "Profiling $design $net"
        python3 src/main.py --model $net --timeloop_dir $design
    done
done
