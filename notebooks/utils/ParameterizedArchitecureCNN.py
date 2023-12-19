import torch.nn as nn
import torch


class ParameterizedArchitectureCNN(nn.Module):
    def __init__(self, kernel_sizes, stride, padding, pool_size, fc_sizes, activation_func, conv_drop, fc_drop):
        super(ParameterizedArchitectureCNN, self).__init__()

        self.conv_layers = nn.ModuleList()
        self.pool_layers = nn.ModuleList()
        self.fc_layers = nn.ModuleList()
        self.in_channels = 4
        self.num_conv_layers = len(kernel_sizes)
        self.num_fc_layers = len(fc_sizes) + 1

        self._create_conv_layers(kernel_sizes, pool_size, stride, padding)

        img_size = [480, 640]
        conv_out_size = self._calculate_conv_output_size(img_size, kernel_sizes, stride, padding, pool_size)

        self._create_fc_layers(fc_sizes, conv_out_size)

        self.activation_func = activation_func
        self.conv_dropout = nn.Dropout2d(p=conv_drop)
        self.fc_dropout = nn.Dropout(p=fc_drop)

    def _create_conv_layers(self, kernel_sizes, pool_size, stride, padding):
        for i in range(self.num_conv_layers):
            out_channels = self.in_channels * 2
            self.conv_layers.append(nn.Conv2d(self.in_channels, out_channels, kernel_sizes[i], stride, padding))
            self.pool_layers.append(nn.MaxPool2d(pool_size, pool_size))
            self.in_channels = out_channels

    def _create_fc_layers(self, fc_sizes, conv_out_size):
        self.fc_layers.append(nn.Linear(self.in_channels * conv_out_size, fc_sizes[0]))
        for i in range(self.num_fc_layers - 2):
            self.fc_layers.append(nn.Linear(fc_sizes[i], fc_sizes[i+1]))
        self.fc_layers.append(nn.Linear(fc_sizes[-1], 21))

    def _calculate_conv_output_size(self, in_size, kernel_sizes, stride, padding, pool_size):
        for i in range(self.num_conv_layers):
            kernel_height, kernel_width = kernel_sizes[i]
            out_height = ((in_size[0] + 2 * padding - kernel_height) // stride) + 1
            out_height = out_height // pool_size
            out_width = ((in_size[1] + 2 * padding - kernel_width) // stride) + 1
            out_width = out_width // pool_size
            in_size[0] = out_height
            in_size[1] = out_width
        return out_width * out_height

    def _forward_conv(self, x):
        for conv_layer, pool_layer in zip(self.conv_layers, self.pool_layers):
            x = self.activation_func(self.conv_dropout(conv_layer(x)))
            x = pool_layer(x)
        return x

    def _forward_fc(self, x):
        for i in range(self.num_fc_layers - 1):
            x = self.activation_func(self.fc_dropout(self.fc_layers[i](x)))
        x = self.fc_layers[-1](x)
        return x

    def forward(self, x):
        x = self._forward_conv(x)
        x = torch.flatten(x, 1)
        x = self._forward_fc(x)

        return x
