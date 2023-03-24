Created: 2022-03-24 10:06

Convolutional neural network is a class of Artificial Neural Network most commonly used to analyze visual imagery (but not only).
The NNs that belong to this class are specialized for grid-like data (like images).

They are inspired by biological processes, in the sense that the connectivity pattern between neurons resembles the organization of the animal visual cortex.

A CNN typically has three layers: a convolutional layer, a pooling layer, and a fully connected layer.

### Convolutional Layer
This layer performs a dot product between two matrices, where one matrix is the set of learnable parameters otherwise known as a kernel, and the other matrix is the restricted portion of the receptive field. The kernel is spatially smaller than an image, but is more in-depth. This means that, if the image is composed of three (RGB) channels, the kernel height and width will be spatially small, but the depth extends up to all three channels.

The input is a tensor with a shape: (number of inputs)x(input height)x(input width)x(input channels).
As the convolution kernel slides along the input matrix for the layer, the convolution operation generates a feature map, which in turn contributes to the input of the next layer.

The sliding size of the kernel is called *"stride"*.

Given an input of size W x W x D and $D_{out}$ number of kernels with a spatial size of F with stride S and amount of padding P, then the size of the output is obtained with: 
$W_{out}=\dfrac{W-F+2P}{S}+1$. 

Convolution leverages three important ideas that motivated computer vision researchers: **sparse interaction**, **parameter sharing**, and **equivariant representation**.

##### Sparse interaction
Usually neural network layers use matrix multiplication in a way in which every output unit interacts with every input unit. In CNNs, we are using kernel, which are smaller than the input, and we can detect meaningful information and at the same time reduce memory requirement of the model.

##### Parameter sharing
When parameters are shared, for getting output, weights applied to one input are the same as the weight applied elsewhere.

##### Equivariance to translation
Thanks to parameter sharing, CNNs are equivariant to translations, i.e. if we change the input in a way, the output will also get changed in the same way.

### Pooling layer
Pooling layers provide an approach to down sampling feature maps by summarizing the presence of features in patches of the feature map. This helps in reducing the spatial size of the representation.
There are several approaches, but the two most famous are *average pooling* and *max pooling*.

### Fully connected layer
Neurons in this layer have full connectivity with all neurons in the preceding and succeeding layer as seen in regular FCNN. This is why it can be computed as usual by a matrix multiplication followed by a bias effect.

The FC layer helps to map the representation between the input and the output.


Since convolution is a linear operation and images are not, non-linear layers are added after the convolutional layer ⇾ sigmoid, tanh, ReLU atc.

## Applications
1. Object detection -> YOLO, Fast R-CNN;
2. Semantic segmentation;
3. Image Captioning;
4. CNNs can help to eliminate the [[Cold-start]] problem or to empower [[Collaborative filtering]] systems.

Good fit for unstructured multimedia data (Images, text etc.) and also for non-Euclidean data ([[Social information]]), thanks to Graph CNNs.

## Limits
1. They fail to encode the position and orientation of objects;
2. A lot of data is needed;
3. Slow because of operations like maxpool;
4. CNNs see clusters of pixels which are arranged in distinct patterns, they do not see them as components present in the image.


## References
1. [Wikipedia](https://en.wikipedia.org/wiki/Convolutional_neural_network)
2. [Towards Data Science](https://towardsdatascience.com/convolutional-neural-networks-explained-9cc5188c4939)
3. https://medium.com/sciforce/deep-learning-based-recommender-systems-b61a5ddd5456


#### Tags
#cnn