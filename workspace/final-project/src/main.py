import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.models as models
import logging
import sys
import argparse
from profiler import count_activation_size
from profiler import Profiler


parser = argparse.ArgumentParser()
parser.add_argument("--model", type=str, default="alexnet")
parser.add_argument("--design", type=str, default="simple_weight_stationary")
args = parser.parse_args()

exp_name = f"{args.model}-{args.design}"
targets = logging.StreamHandler(sys.stdout), logging.FileHandler(f"logs/{exp_name}.log")
logging.basicConfig(format="%(message)s", level=logging.INFO, handlers=targets)

model_dict = {
    "alexnet1": models.alexnet,
    "alexnet": models.alexnet,
    "resnet18": models.resnet18,
    "resnet34": models.resnet34,
    "resnet50": models.resnet50,
    "vgg11": models.vgg11,
    "vgg16": models.vgg16,
    "mobilenet_v2": models.mobilenet_v2,
    "squeezenet1_1": models.squeezenet1_1,
    "densenet121": models.densenet121,
}

model = model_dict[args.model]()

if args.model == "alexnet1":
    # sanity check, single layer alexnet
    model = nn.Sequential(
        nn.Conv2d(3, 64, kernel_size=11, stride=4, padding=2),
        nn.ReLU(inplace=True),
    )


peak_activation_size = count_activation_size(
    net=model,
    input_size=(1, 3, 224, 224),
)

logging.info("Peak Activation Sizes: {} Byte".format(peak_activation_size))


profiler = Profiler(
    top_dir="workloads",
    sub_dir=args.model,
    design=args.design,
    model=model,
    input_size=(3, 224, 224),
    batch_size=1,
    convert_fc=True,
    exception_module_names=[],
    profiled_lib_dir=f"{exp_name}.json",
)

layer_wise_info, overall = profiler.profile()

for layer_id, info in layer_wise_info.items():
    logging.info(
        "Name: {} \t Energy: {:.2f} \t Cycle: {} \t Number of same architecture layers: {}".format(
            info["name"], info["energy"], info["cycle"], info["num"]
        )
    )

logging.info("Total Energy: {:.8f} mj".format(overall["total_energy"] / 1e3))
logging.info("Total Cycles: {:.8f} Million".format(overall["total_cycle"] / 1e6))
logging.info("MACs: {}".format(overall["macs"]))
logging.info("Num of Parameters: {}".format(overall["num_params"]))
logging.info("Peak Activation Size: {} Byte".format(overall["activation_size"]))
