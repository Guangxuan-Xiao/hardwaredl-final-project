DESIGNS="simple_weight_stationary eyeriss"
NETS="squeezenet1_1 resnet18 alexnet"
for net in $NETS; do
    for design in $DESIGNS; do
        echo "Profiling $design $net"
        python3 src/main.py --model $net --design $design
    done
done
