DESIGNS="eyeriss_like simple_output_stationary simple_weight_stationary simba_like"
NETS="alexnet vgg11 resnet18 squeezenet1_1"
for net in $NETS; do
    for design in $DESIGNS; do
        echo "Profiling $design $net"
        python3 src/main.py --model $net --design $design
    done
done
