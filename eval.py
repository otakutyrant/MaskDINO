import os
from pathlib import Path

import cv2
from detectron2.config import get_cfg
from detectron2.engine import (
    default_argument_parser,
    default_setup,
)
from detectron2.modeling import build_model
from detectron2.projects.deeplab import add_deeplab_config, build_lr_scheduler
import numpy as np
from maskdino import (
    add_maskdino_config,
)

dataset_path = Path(os.getenv('dataset')) / 'dataset' # TODO
CONFIG_FILE = 'configs/seg-poc/maskdino_R50_bs16_90k_steplr.yaml'
cfg.WEIGHTS = '' # TODO

class Evaluator:
    def __init__(self, cfg=None):
        parser = default_argument_parser()
        args = parser.parse_args()
        if cfg is None:
            cfg = get_cfg()
            # for poly lr schedule
            add_deeplab_config(cfg)
            add_maskdino_config(cfg)
            cfg.merge_from_file(CONFIG_FILE) # TODO
            cfg.freeze()
            default_setup(cfg, args)
        self.predicator = DefaultPredictor(cfg)

    def forward(image: np.ndarray):
        return self.predicator(image)

def generate_labels(dataset_path=dataset_path, output_dir=None):
    evaluator = Evaluator()
    if output_dir is None:
        output_dir = dataset_path / 'labels'

    for image_path in (dataset_path / 'images').iterdir():
        image = cv2.imread(str(image_path))
        label = forward(image)
        label_path = output_dir / image_path.replace(x, y) # TODO
        cv2.imwrite(str(label_path), label)
