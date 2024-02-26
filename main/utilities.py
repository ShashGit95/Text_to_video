# import cv2
# import numpy as np
# from typing import List, Union
# import PIL.Image
# import tempfile

# def resize_frame(frame: np.ndarray, target_shape: tuple) -> np.ndarray:
#     """
#     Resize a frame to the target shape.
    
#     Args:
#         frame: Input frame as a numpy array.
#         target_shape: Desired shape of the frame (width, height).
    
#     Returns:
#         Resized frame as a numpy array.
#     """
#     return cv2.resize(frame, target_shape)

# def export_to_video(
#     video_frames: Union[List[np.ndarray], List[PIL.Image.Image]],
#     output_video_path: str = None,
#     fps: int = 8,
#     target_shape: tuple = None
# ) -> str:
#     if output_video_path is None:
#         output_video_path = tempfile.NamedTemporaryFile(suffix=".mp4").name

#     if isinstance(video_frames[0], PIL.Image.Image):
#         video_frames = [np.array(frame) for frame in video_frames]

#     fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    
#     if target_shape is None:
#         # Use the shape of the first frame if target shape is not provided
#         h, w, c = video_frames[0].shape
#         target_shape = (w, h)
    
#     video_writer = cv2.VideoWriter(output_video_path, fourcc, fps=fps, frameSize=target_shape)
    
#     for frame in video_frames:
#         if frame.shape[:2] != target_shape:
#             frame = resize_frame(frame, target_shape)
#         img = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
#         video_writer.write(img)
    
#     video_writer.release()
    
#     return output_video_path

# import cv2
# import numpy as np
# from typing import List, Union
# import PIL.Image
# import tempfile

# def export_to_video(
#     video_frames: Union[List[np.ndarray], List[PIL.Image.Image]],
#     output_video_path: str = None,
#     fps: int = 8
# ) -> str:
    
#     if output_video_path is None:
#         output_video_path = tempfile.NamedTemporaryFile(suffix=".mp4").name

#     if isinstance(video_frames[0], PIL.Image.Image):
#         video_frames = [np.array(frame) for frame in video_frames]

#     fourcc = cv2.VideoWriter_fourcc(*"mp4v")
  

#     h, w, c = video_frames.shape[2:5]

#     if output_video_path is None:
#         output_video_path = "output_video.mp4"
  

#     video_writer = cv2.VideoWriter(output_video_path, fourcc, fps=fps, frameSize=(w, h))
#     for i in range(len(video_frames)):
#         img = cv2.cvtColor(video_frames[i], cv2.COLOR_RGB2BGR)
#         video_writer.write(img)
#     return output_video_path

# 3rd code

import cv2
import numpy as np
from typing import List, Union
import PIL.Image
import tempfile

# def export_to_video(
#     video_frames: Union[List[np.ndarray], List[PIL.Image.Image]],
#     output_video_path: str = None,
#     fps: int = 8
# ) -> str:
#     if output_video_path is None:
#         output_video_path = tempfile.NamedTemporaryFile(suffix=".mp4").name

#     if isinstance(video_frames[0], PIL.Image.Image):
#         video_frames = [np.array(frame) for frame in video_frames]

#     fourcc = cv2.VideoWriter_fourcc(*"mp4v")

#     # Extract frame dimensions
#     batch_size, num_frames, height, width, channels = video_frames.shape

#     # Initialize VideoWriter object
#     video_writer = cv2.VideoWriter(output_video_path, fourcc, fps=fps, frameSize=(width, height))

#     # Write frames to video
#     for i in range(num_frames):
#         # Extract frame from the batch
#         frame = video_frames[0, i]
#         # Convert frame to BGR format (OpenCV uses BGR color ordering)
#         img = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
#         video_writer.write(img)

#     # Release VideoWriter object
#     video_writer.release()

#     return output_video_path

def export_to_video(
    video_frames: Union[List[np.ndarray], List[PIL.Image.Image]], output_video_path: str = None, fps: int = 8
) -> str:
   
    if output_video_path is None:
        output_video_path = tempfile.NamedTemporaryFile(suffix=".mp4").name

    if isinstance(video_frames[0], PIL.Image.Image):
        video_frames = [np.array(frame) for frame in video_frames]

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    h, w, c = video_frames[0].shape
    
    video_writer = cv2.VideoWriter(output_video_path, fourcc, fps=fps, frameSize=(w, h))
    for i in range(len(video_frames)):
        img = cv2.cvtColor(video_frames[i], cv2.COLOR_RGB2BGR)
        video_writer.write(img)