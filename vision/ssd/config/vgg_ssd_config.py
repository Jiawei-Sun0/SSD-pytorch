import numpy as np

from vision.utils.box_utils import SSDSpec, SSDBoxSizes, generate_ssd_priors


image_size = 300
image_mean = np.array([123, 117, 104])  # RGB layout
image_std = 1.0

iou_threshold = 0.45
center_variance = 0.1
size_variance = 0.2

if image_size == 300:
    specs = [
        SSDSpec(38, 8, SSDBoxSizes(30, 60), [2]),
        SSDSpec(19, 16, SSDBoxSizes(60, 111), [2, 3]),
        SSDSpec(10, 32, SSDBoxSizes(111, 162), [2, 3]),
        SSDSpec(5, 64, SSDBoxSizes(162, 213), [2, 3]),
        SSDSpec(3, 100, SSDBoxSizes(213, 264), [2]),
        SSDSpec(1, 300, SSDBoxSizes(264, 315), [2])
    ]
if image_size == 400:
    specs = [
        SSDSpec(25, 16, SSDBoxSizes(60, 105), [2, 3]),
        SSDSpec(13, 32, SSDBoxSizes(105, 150), [2, 3]),
        SSDSpec(7, 64, SSDBoxSizes(150, 195), [2, 3]),
        SSDSpec(4, 100, SSDBoxSizes(195, 240), [2, 3]),
        SSDSpec(2, 150, SSDBoxSizes(240, 285), [2, 3]),
        SSDSpec(1, 300, SSDBoxSizes(285, 330), [2, 3])
    ]

priors = generate_ssd_priors(specs, image_size)