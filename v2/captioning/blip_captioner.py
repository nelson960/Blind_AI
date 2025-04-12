from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch
import numpy as np

class BLIPCaptioner:
    def __init__(self):
        self.device = "mps" if torch.backends.mps.is_available() else "cpu"
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to(self.device)

    def caption(self, frame):
        image = Image.fromarray(frame.astype(np.uint8))
        inputs = self.processor(image, return_tensors="pt").to(self.device)
        out = self.model.generate(**inputs)
        return self.processor.decode(out[0], skip_special_tokens=True)
