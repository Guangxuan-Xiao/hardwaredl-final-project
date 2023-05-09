nn="alexnet"
layer="6"
arch="eyeriss_like"
timeloop-mapper designs/${arch}/arch/${arch}.yaml designs/${arch}/arch/components/*.yaml designs/${arch}/mapper/mapper.yaml designs/${arch}/constraints/*.yaml workloads/${nn}/${nn}_layer${layer}.yaml