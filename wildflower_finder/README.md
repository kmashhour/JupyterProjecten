# 🌼 Wildflower Finder
This notebook shows a simplified implementation for a wildflower object detection model. Images are top-down photos of fields and meadows including wildflowers, which the model is supposed to detect and classify. Note that this is an actual case that was addressed by the Fontys ICT AI & Data research group in 2023 and produced the academic paper [Data-centric AI Approach for Automated Wildflower Monitoring](https://doi.org/10.1371/journal.pone.0302958) (Schouten G, Michielsen BSHT, Gravendeel B, 2024). The original dataset has many more species and larger images and can be found at [Eindhoven Wildflower Dataset](https://doi.org/10.34894/u4vqj6) (Schouten G & Michielsen BSHT, 2024), feel free to use the original data set in your own work if you want to.

![banner](https://codeberg.org/Fontys/wildflower_finder/raw/branch/main/BANNER.jpg)

*Image by Stable Diffusion: a robot looking for wildflowers in a meadow*

This notebook is intentionally designed as a foundational starting point and does not strictly adhere to established best practices as it is meant as a learning opportunity. This repo belongs to a five part course:&nbsp;&nbsp;&nbsp; 🏠&nbsp;[House&nbsp;Price&nbsp;Predictor](https://codeberg.org/Fontys/house_price_predictor)&nbsp;&nbsp;&nbsp; 👗&nbsp;[Clothing&nbsp;Sorter](https://codeberg.org/Fontys/clothing_sorter)&nbsp;&nbsp;&nbsp; 💬&nbsp;[Expert&nbsp;Chat](https://codeberg.org/Fontys/expert_chat)&nbsp;&nbsp;&nbsp; 🌼&nbsp;[Wildflower&nbsp;Finder](https://codeberg.org/bshtmichielsen/wildflower_finder)&nbsp; Feel free to learn from the other parts too!

## 📚 Preparation
Please ensure that you are familiar with the following aspects in order to successfully work with this repo and notebook.
 - You can distinguish [object detection from image classification](https://www.augmentedstartups.com/blog/object-detection-vs-classification-in-computer-vision-explained).
 - Explain the role of bounding boxes and what [Intersection‑over‑Union](https://blog.unitlab.ai/intersection-over-union-iou/) measures.
 - You can describe the components of Faster R‑CNN: Region Proposal Network (RPN), ROI pooling, classification & regression heads.
 - Explain the typical evaluation metrics for object detection, [mean average precision](https://www.geeksforgeeks.org/computer-vision/mean-average-precision-map-in-computer-vision/) at certain intersection over union values.

## 🎯 Learning opportunities
The following aspects of machine learning are part of this example:
 - Load and visualize image datasets with annotations.
 - Use a pre‑trained Faster R‑CNN model and fine‑tune it on a custom dataset.
 - Implement a custom data loader that returns images, bounding boxes, and class labels.
 - Evaluate detection performance using mean Average Precision (mAP) and analyze failure cases.
 - Visualize predictions: draw bounding boxes with confidence scores and class names on test images.

## 🤔 Considerations
The following is a list of considerations for improvement or for your own project.
 - During training we simply sum the losses of all the components of the network, it may have been nice to have them logged and visualized.
 - The validation metric we use during training (mAP over all classes) makes sense to use as a simple indicator for the quality of the model during training. It is an easy enough metric to monitor against and decide whether to stop training early. However, as a test metric it is less suited as it is a combination of several things. The current implementation addresses this issue by calculating mAP per class, which is already a lot better. However, it may be even better to instead separately calculate and reports its components per class. Think about Intersection over Union for example.
 - The current learning rate scheduler using a step based approach, it simply decays the learning rate of each parameter group by its gamma after every of its set number of epochs. Maybe a scheduler that decays the learning rate in an incremental way may be better suited? Or perhaps one that waits for the moment that the current state no longer produces improvement and then reduces the learning rate? Can you visualize the learning rate's progression over epochs?
 - In the evaluation you can see that for some species the model completely misses detection of the wildflower (recall), for example Plantago Lanceolata. Given that it is this model's primary task to find wildflower, we can argue that missing one completely is the worst kind of error (perhaps even worse than misclassification) therefore the model's component that makes region proposals (ROI) is likely more important that its classification component. It may be interesting to figure out if we can use a different learning rate strategy for the region proposal components as to let it learn a bit better.

## ⭐ Citation & Star
If you use my work please cite and star ⭐ this repo. Thanks!

> Michielsen, Bas S.H.T. (2026) "Wildflower Finder" Codeberg: https://codeberg.org/Fontys/wildflower_finder