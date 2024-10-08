# DDCNet
  The parameter count of existing models limits their applicability on resourceconstrained devices. To address these challenges, this paper introduces a DetailEnhanced Lightweight Network (DDCNet) for small object detection. DDCNet incorporates a Detail Feature Compensation Module at downsampling layers to
recover lost detail information, a Detail Feature Enhancement Module between the backbone and neck to enhance detail features, and a Cross-Scale Detail
Feature Fusion Module to merge multi-scale information. Experimental results demonstrate that DDCNet achieves state-of-the-art performance with a parameter
count of only 1.75M, obtaining mAP50 scores of 48.9% and 55.4% on the Visdrone and AI-TOD datasets, respectively. Our work presents a novel solution
to the issue of feature loss due to downsampling in small object detection, offering a balance between detection performance and model efffciency.

![DDCNet](https://github.com/user-attachments/assets/c375dd24-f236-44ec-bc10-9f686e8ddcee)


If you want to train DDCNet, just install the required environment for YOLOv8 and click on the main file in your home directory.


