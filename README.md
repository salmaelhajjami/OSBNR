# OSBNR: One Side Behavioral Noise Reduction

OSBNR (One Side Behavioral Noise Reduction) is an approach developed to deal with the problem of class imbalance in the presence of behavioral noise. This method is based on two stages: clustering and reduction. In the clustering stage, k-means algorithm is used to group similar instances of the minority class into multiple behavior clusters, each with distinct characteristics in the high-dimensional feature space. In the reduction stage, instances of the majority class, considered as behavioral noise, which overlap with the behavior clusters of the minority class are selected and eliminated.

The main steps of OSBNR approach are:

1. Separate: Separate the majority class and minority class from the original training dataset.
2. Clustering: Apply k-means clustering to group similar minority class instances into behavior clusters.
3. Reduction: Eliminate the noisy majority class instances that overlap with the behavior clusters of the minority class.
4. Combination: Combine the reduced majority class instances with the minority class instances to form a new training dataset.

Accurate identification and elimination of these instances maximize the visibility of the minority class instances and at the same time minimize excessive elimination of data.
  
This approach has been applied to various domains, including fraud detection, anomaly detection, and imbalanced datasets.

## Usage

To use OSBNR, you can simply import the OSBNR class from the PyOSBNR module and create an instance of the class with the desired number of clusters (k). Then, by calling the fit_resample method of the OSBNR instance, you can obtain the balanced feature matrix and label vector.

Here's an example code :

    from PyOSBNR import OSBNR

    osbnr = OSBNR(k=5)  # Create an instance of the OSBNR class with k=5 clusters
    X_resampled, y_resampled = osbnr.fit_resample(X, y)  # Resample the dataset using OSBNR

With just a few lines of code, you can easily leverage the power of OSBNR to address class imbalance in your dataset and obtain more accurate results in your machine learning models.

## Installation

To install OSBNR, use pip:

    pip install PyOSBNR

## License

This project is licensed under the GNU License - see the LICENSE file for details.

## Publications 

- El Hajjami, S., Malki, J., Bouju, A., & Berrada, M. (2020, October). A machine learning based approach to reduce behavioral noise problem in an imbalanced data: application to a fraud detection. In 2020 International Conference on Intelligent Data Science Technologies and Applications (IDSTA) (pp. 11-20). IEEE.

- El Hajjami, S., Malki, J., Berrada, M., & Fourka, B. (2020, November). Machine learning for anomaly detection. performance study considering anomaly distribution in an imbalanced dataset. In 2020 5th International Conference on Cloud Computing and Artificial Intelligence: Technologies and Applications (CloudTech) (pp. 1-8). IEEE.

- El Hajjami, S., Malki, J., Bouju, A., & Berrada, M. (2021). Machine Learning Facing Behavioral Noise Problem in an Imbalanced Data Using One Side Behavioral Noise Reduction: Application to a Fraud Detection. International Journal of Computer and Information Engineering, 15(3), 194-205.
