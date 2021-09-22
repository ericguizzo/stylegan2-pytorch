import os
import tempfile
from pathlib import Path

import cog

class Predictor(cog.Predictor):
    def setup(self):
        """Load the model"""
        # Setup

    @cog.input("input", type=Path, help="Input image path")
    def predict(self, seed, sampling_type, output_type):
        """Compute prediction"""
        print ("mbescill' demmierd'")
