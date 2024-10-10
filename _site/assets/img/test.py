import numpy as np
from PIL import Image, ImageDraw, ImageFont
import imageio

def add_noise(image, noise_level):
    # Convert the image to a numpy array
    image_array = np.array(image).astype(np.float32) / 255.0
    # Generate noise
    noise = np.random.uniform(-noise_level, noise_level, image_array.shape)
    # Add noise and clip the result to be between 0 and 1
    noisy_image_array = np.clip(image_array + noise, 0, 1)
    # Convert the array back to an image
    noisy_image = Image.fromarray((noisy_image_array * 255).astype(np.uint8))
    return noisy_image

def generate_noise_transition_gif(input_image_path, output_gif_path, num_frames=20):
    # Load the initial image
    original_image = Image.open(input_image_path)
    
    frames = []
    
    # Create frames for adding noise
    # for i in range(num_frames):
    #     noise_level = i / num_frames
    #     noisy_image = add_noise(original_image, noise_level)
    #     frames.append(noisy_image)
    
    # Create frames for removing noise (reverse process)
    for i in range(num_frames, -1, -1):
        noise_level = i / num_frames
        k = num_frames-i
        noisy_image =original_image
        for j in range(k):
            noisy_image = add_noise(noisy_image, noise_level)
        frames.append(noisy_image)
    
    # Save frames as a GIF
    imageio.mimsave(output_gif_path, [np.array(frame) for frame in frames], duration=0.1)

# Example usage
generate_noise_transition_gif('./teng.jpg', 'teng.gif', num_frames=30)
