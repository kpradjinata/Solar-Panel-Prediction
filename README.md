# Solar Panel Image Classification

Solar panels are crucial for generating clean energy, and their efficiency is impacted by environmental factors such as soiling and solar irradiance. This project focuses on classifying solar panel images based on the extent of soiling and the amount of solar irradiance, using deep learning techniques. The goal is to automate the detection of common flaws in solar panels, reducing manual inspection efforts and contributing positively to the solar energy community.

## Overview

### Purpose

The purpose of this project is to develop a model that classifies solar panel images, considering factors like soiling and solar irradiance. By automating this classification, we aim to enhance the efficiency of solar panels and minimize power loss.

### Key Environmental Factors

1. **Soiling:** Accumulation of dirt and dust on solar panels, blocking sunlight and decreasing power output.
2. **Solar Irradiance:** Total power per unit area received from the sun, influenced by factors like time of day, weather conditions, and time of year.

## Methodology

### Data Collection

- **Dataset:** Deep Solar Eye dataset with approximately 45,000 solar panel images.
- **Variables:** Power loss (percentage of optimal power), Solar Irradiance.

### Primary Model

1. **Input Data Organization:** Images categorized into high, medium, and low power loss folders.
2. **Model Architecture:** Basic model with Conv2D, MaxPooling2D, and Dense layers.
3. **Optimization:** Determined optimal batch size and epochs for highest accuracy (53%).

### Final Model

1. **Input Pipeline Enhancements:** Implemented `Dataset.cache()` and `Dataset.prefetch()` for better performance.
2. **Overfitting Prevention:** Applied data augmentation and dropouts to combat overfitting.
3. **Incorporating Solar Irradiance:** Multiplied power loss by irradiance, simplifying the model without significant accuracy loss.

## Results

- **Accuracy:** Improved from 53% in the primary model to 82% in the final model.
- **Individual Image Testing:** Successfully classified individual images with high confidence.

## Limitations and Future Considerations

- **Dataset Limitations:** Limited datasets for specific environmental conditions.
- **Other Factors:** Model doesn't address issues like snail trails and microcracks.
- **Hardware Limitations:** Processing time for large datasets on standard hardware.

### Transfer Learning (Future Work)

Explore transfer learning with pretrained models to potentially boost accuracy without extensive training on solar panel images.

## Acknowledgments

- **Mr. Suresh Subramaniam:** For guidance and support in machine learning and Python.
- **Olive Children Foundation and ASDRP:** Providing the opportunity for conducting research.

## Contact Information

For inquiries and correspondence, please reach out to suresh.subramaniam@fremontstem.com.

## Bibliography

1. Top five solar panel uses. [Link](https://modernize.com/home-ideas/29961/top-five-solar-panel-uses)
2. Sachin Mehta, et al. "Deepsolareye: Power loss prediction and weakly supervised soiling localization." Oct 2017.
3. BD Editors. "What is solar irradiance." [Link](https://biologydictionary.net/what-is-solar-irradiance/)
4. "Deep learning for image classification with less data." [Link](https://www.kdnuggets.com/2019/11/deep-learning-image-classification-less-data.html)
5. Abdellatif Abdelfattah. "Image classification using deep neural networks." Oct 2017.
6. Martin Heller. "What is keras? The deep neural network API explained." Jan 2019.
7. TensorFlow. "Image classification: TensorFlow core." [Link](https://www.tensorflow.org/tutorials/images/classification)
8. Jason Brownlee. "Dropout regularization in deep learning models with Keras." Sep 2019.
9. Philip J. Harrison, Alexander Kensert. "Transfer learning with deep convolutional neural networks for classifying cellular morphological changes." 2019.
