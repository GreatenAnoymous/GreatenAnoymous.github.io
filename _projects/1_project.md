---
layout: page
title: project 1
description: Enhanced FoundationPose For Pose Estimation and Tracking
img: assets/video/demo_head.gif
importance: 1
category: work
related_publications: false
---
FoundationPose is a state-of-the-art vision foundation model for 6D pose estimation and pose tracking. For pose estimation, it leverages the CAD model, RGBD input, and the object's mask. The process involves:

1. Generating globally sampled random pose hypotheses.
2. Refining these hypotheses using a refinement network.
3. Scoring each pose with a scoring network, with the highest-scoring pose selected as the final result.
For pose tracking, FoundationPose initializes the pose hypotheses using the pose from the previous frame and refines it with the same refinement network.

Enhancements Introduced:
1. Depth-Free Operation: The model now supports pose estimation and tracking without requiring depth input.
2. Robust Object Tracking: Improved tracking resilience, enabling recovery from tracking losses.

The following sections include demonstration comparisons showcasing these enhancements.

Firstly, we demonstrate that when the input depth is of poor quality (e.g., in the demo where depth is captured by a D404 sensor), the original FoundationPose struggles to achieve accurate pose estimation and tracking. In contrast, our enhanced version performs effectively without relying on depth input.
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid path="assets/video/demo1.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true %}
    </div>
</div>

Secondly, we demonstrate that when monocular depth obtained from the zero-shot metric depth estimation model, ZoeDepth, is used as input, the original FoundationPose fails to perform effectively. In contrast, our enhanced version continues to deliver robust results.
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid path="assets/video/demo2.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true %}
    </div>
</div>


Thirdly, we demonstrate that when the tracked object is temporarily occluded by other objects, the original FoundationPose loses tracking and fails to recover. In contrast, our enhanced version, integrating XMem and a linear Kalman filter, provides more robust object tracking. Additionally, the enhanced pipeline achieves real-time performance, running at 20-30 FPS on an RTX 3090 with a 640×480 image resolution
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid path="assets/video/demo3.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true %}
    </div>
</div>

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid path="assets/video/demo4.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true %}
    </div>
</div>
