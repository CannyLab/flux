"""
Vision data loading utilities
"""

from typing import Tuple
import numpy as np
from flux.util.logging import log_warning

try:

    import cv2

    def load_image(fpath: str) -> np.ndarray:
        """Load an image from string
    
        Arguments:
            fpath {str} -- The file path of the image to load
        """
        image = cv2.imread(fpath)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return image

    def resize_image(image: np.ndarray, shape: Tuple[int, int]) -> np.ndarray:
        image = cv2.resize(image, (shape[0], shape[1]), interpolation=cv2.INTER_CUBIC)
        return image


except ImportError as ex:
    print(ex)
    log_warning('Error trying to import CV2 - To use the vision modules make sure opencv is installed.')
