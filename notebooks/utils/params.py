import torch.nn as nn


architecture_params = [{
    "kernel_sizes": [(10, 3), (3, 10), (5, 5)],
    "stride": 1,
    "padding": 1,
    "pool_size": 2,
    "fc_sizes": [1000, 64],
    "epochs": 10,
    "conv_dropout": 0.3,
    "fc_dropout": 0.0,
    "activation_func": nn.ReLU(),
    "learning_rate": 0.0005
},
{
    "kernel_sizes": [(10, 3), (3, 10), (5, 5)],
    "stride": 1,
    "padding": 1,
    "pool_size": 2,
    "fc_sizes": [1000, 64],
    "epochs": 8,
    "conv_dropout": 0.3,
    "fc_dropout": 0.0,
    "activation_func": nn.ReLU(),
    "learning_rate": 0.0001
}
]

tags_list = ['guitar',
             'classical',
             'slow',
             'techno',
             'strings',
             'drums',
             'electronic',
             'rock',
             'fast',
             'piano',
             'ambient',
             'beat',
             'violin',
             'synth',
             'female',
             'indian',
             'opera',
             'quiet',
             'flute',
             'choir',
             'cello']
