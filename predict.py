import os
import tempfile
from pathlib import Path

import cog
import torch
from torchvision.utils import save_image
from stylegan2_pytorch import ModelLoader

class Predictor(cog.Predictor):
    def setup(self):
        """Load the model"""
        # Setup

    @cog.input("input", type=Path, help="Input image path")
    def predict(self, seed, sampling_type, output_type):
        """Compute prediction"""
        print ("mbescill' demmierd'")
