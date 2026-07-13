---
title: "Gradslam"
url: "/gradslam/"
aliases: ["/Gradslam/"]
categories: []
lastmod: "2022-07-25T09:21:57Z"
---

See https://gradslam.github.io/

## Description
Gradslam (or ∇SLAM) is used for instant reality capture. It is an open-source framework providing differentiable building blocks for simultaneous localization and mapping (SLAM) systems. We enable the usage of dense SLAM subsystems from the comfort of PyTorch.

SLAM technology can be used in a number of different settings. The foremost use case is mapping spaces: using RGB-D cameras or LiDAR, a (coloured) point cloud or mesh can be created. It is a relatively low-cost solution, compared to laser scanning with a TLS (however not as accurate) and a lot faster than traditional photogrammetry methods. 

Gradslam is a fully differentiable dense SLAM framework. It provides a repository of differentiable building blocks for a dense SLAM system, such as differentiable nonlinear least squares solvers, differentiable ICP (iterative closest point) techniques, differentiable raycasting modules, and differentiable mapping/fusion blocks. One can use these blocks to construct SLAM systems that allow gradients to flow all the way from the outputs of the system (map, trajectory) to the inputs (raw color/depth images, parameters, calibration, etc.).

License: 
Source: [MIT](/mit/)

## External Reference
- About: https://gradslam.github.io/
- Github: https://github.com/gradslam/gradslam
- Documentation: https://gradslam.readthedocs.io/en/latest/
- A longer technical report of ICRA 2020 paper: https://arxiv.org/abs/1910.10672
