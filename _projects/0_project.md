---
layout: page
title: project 0
description: Robotic Grasping of Transparent Objects Using Mono Depth Estimation Model
img: assets/video/Demo4.gif
importance: 1
category: work
related_publications: false
---

We fine-tuned the Depth-Anything model using LoRA on mixed public transparent object datasets to estimate the relative depth of transparent objects. Additionally, we proposed a one-shot alignment method for rapid deployment of the model on real robots. Combined with GraspNet and SuctionNet for predicting grasping poses, the UR5 robot can robustly grasp transparent objects without the aid of depth sensors.


<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/video/Demo4.gif" title="" class="img-fluid rounded z-depth-1" %}
    </div>
</div>



<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/video/Demo3.gif" title="" class="img-fluid rounded z-depth-1" %}
    </div>
</div>