Stable Diffusion ControlNet의 원리를 활용하여 간단한 해킹을 통해 옛날 사진을 복원하고 물체를 지우는(Inpainting) 모델

- Stable Diffusion 2.1 Inpainting
- ControlNet Canny
- Scratch Detection

### Install requirements

```python
#@title Install requirements

!git clone https://github.com/vijishmadhavan/UnpromptedControl
%cd UnpromptedControl
!pip install -q gradio
!pip install -q diffusers==0.14.0 xformers transformers scipy ftfy accelerate controlnet_aux
!pip install -q opencv-contrib-python
!wget -q https://www.dropbox.com/s/5jencqq4h59fbtb/FT_Epoch_latest.pt
```

### Load Models

```python
#@title Load Models

import gradio as gr
import numpy as np
import torch
from src.pipeline_stable_diffusion_controlnet_inpaint import *
from scratch_detection import ScratchDetection, process_images
from diffusers import StableDiffusionInpaintPipeline, ControlNetModel, DEISMultistepScheduler
from diffusers.utils import load_image
from PIL import Image
import cv2
import time
import os

device = "cuda"

controlnet = ControlNetModel.from_pretrained("thepowefuldeez/sd21-controlnet-canny", torch_dtype=torch.float16)

pipe = StableDiffusionControlNetInpaintPipeline.from_pretrained(
    "stabilityai/stable-diffusion-2-inpainting", controlnet=controlnet, torch_dtype=torch.float16
)

pipe.scheduler = DEISMultistepScheduler.from_config(pipe.scheduler.config)

# speed up diffusion process with faster scheduler and memory optimization
# remove following line if xformers is not installed
pipe.enable_xformers_memory_efficient_attention()
pipe.to('cuda')

print("Models loaded successfully!")
```

### Image

```python
!wget -q https://github.com/microsoft/Bringing-Old-Photos-Back-to-Life/blob/master/test_images/old_w_scratch/a.png?raw=true -O /content/test.png
img = Image.open("/content/test.png").convert("RGB")
```

### Detect scratches from the image

```python
process_images("/content", "/content/mask", input_size="scale_256", gpu=0)

mask_img = Image.open("/content/mask/mask/test.png")

import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(16, 10))

axes[0].imshow(img)
axes[1].imshow(mask_img)
axes[0].axis("off")
axes[1].axis("off")
plt.tight_layout()
plt.show()
```

![image](https://github.com/user-attachments/assets/f71b9148-4848-4efc-b09e-5c90547d37f7)


### Dilated the mask image

```python
mask_img_resized = mask_img.resize(img.size, Image.BICUBIC)

# Apply dilation to make the lines bigger
kernel = np.ones((5, 5), np.uint8)
mask_img_np = np.array(mask_img_resized)
mask_img_np_dilated = cv2.dilate(mask_img_np, kernel, iterations=2)
mask_img_dilated = Image.fromarray(mask_img_np_dilated)

fig, axes = plt.subplots(1, 2, figsize=(16, 10))

axes[0].imshow(mask_img)
axes[1].imshow(mask_img_dilated)
axes[0].axis("off")
axes[1].axis("off")
plt.tight_layout()
plt.show()
```

![image](https://github.com/user-attachments/assets/b259ea27-136c-4f3f-9c57-21228119edf0)


### Canny edge detection from the image

```python
input_img = np.array(img)

low_threshold = 100
high_threshold = 200
canny = cv2.Canny(input_img, low_threshold, high_threshold)
canny = canny[:, :, None]
canny = np.concatenate([canny, canny, canny], axis=2)
canny_img = Image.fromarray(canny)

canny_img
```

![image](https://github.com/user-attachments/assets/68c0a9cb-708b-4f0c-8c36-57f9987c733b)


### Inpaint with Stable Diffustion ControlNet

```python
output = pipe(
	propt = "",
	num_inference_steps = 100,
	generator = torch.manual_seed(0),
	image = input_img,
	control_image = canny_img,
	controlnet_conditioning_scale = 0,
	mask_image = mask_img_dilated,
)/images[0]
```

### Result

```python
fig, axes = plt.subplots(1, 2, figsize=(16, 10))

axes[0].imshow(img)
axes[1].imshow(output)
axes[0].axis("off")
axes[1].axis("off")
plt.tight_layout()
plt.show()
```

![image](https://github.com/user-attachments/assets/7ab6792b-d5b7-4eec-b18f-00dcb982154d)
