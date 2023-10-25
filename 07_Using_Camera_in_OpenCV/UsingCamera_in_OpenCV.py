#!/usr/bin/python

#                          License Agreement
#                         3-clause BSD License
#
#       Copyright (C) 2018, Xperience.AI, all rights reserved.
#
# Third party copyrights are property of their respective owners.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions and the following disclaimer.
#
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
#   * Neither the names of the copyright holders nor the names of the contributors
#     may be used to endorse or promote products derived from this software
#     without specific prior written permission.
#
# This software is provided by the copyright holders and contributors "as is" and
# any express or implied warranties, including, but not limited to, the implied
# warranties of merchantability and fitness for a particular purpose are disclaimed.
# In no event shall copyright holders or contributors be liable for any direct,
# indirect, incidental, special, exemplary, or consequential damages
# (including, but not limited to, procurement of substitute goods or services;
# loss of use, data, or profits; or business interruption) however caused
# and on any theory of liability, whether in contract, strict liability,
# or tort (including negligence or otherwise) arising in any way out of
# the use of this software, even if advised of the possibility of such damage.

import cv2
import sys

# Source of video stream: System Default Camera Device 
s = 0
# We can choose a specific source directly from the command line
if len(sys.argv) > 1:
    s = sys.argv[1]

# Create video capture object
source = cv2.VideoCapture(s)

win_name = 'Camera Preview'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

## Quick fun to save the video

# set resolution using property id
frame_width = int(source.get(cv2.CAP_PROP_FRAME_WIDTH)) # 3
frame_height = int(source.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 4
   
size = (frame_width, frame_height)

# print("size: ", size)
# exit("exit the program")

video_file_name = 'quickfun.avi'
result = cv2.VideoWriter(video_file_name, 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)


while cv2.waitKey(1) != 27: # Escape
    has_frame, frame = source.read()
    if not has_frame:
        break
    # save the video
    result.write(frame)
    
    cv2.imshow(win_name, frame)

source.release()
cv2.destroyWindow(win_name)
