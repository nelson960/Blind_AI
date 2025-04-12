from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

class SceneDescriber:
	def __init__(self):
		self.device = "mps" if torch.backends.mps.is_available() else "cpu"
		self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
		self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to(self.device)

	def describe(self, frame):
		image = Image.fromarray(frame)
		inputs = self.processor(image, return_tensors="pt").to(self.device)
		out = self.model.generate(**inputs)
		caption = self.processor.decode(out[0], skip_special_tokens=True)
		return caption