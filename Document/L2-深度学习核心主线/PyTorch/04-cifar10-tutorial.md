[Skip to main content](#main-content)

__Back to top

__ `Ctrl`+`K`

Rate this Page

★ ★ ★ ★ ★

beginner/blitz/cifar10_tutorial

![](../../_static/img/pytorch-colab.svg) Run in Google Colab Colab ![](../../_static/img/pytorch-download.svg) Download Notebook Notebook ![](../../_static/img/pytorch-github.svg) View on GitHub GitHub

Note

[Go to the end](#sphx-glr-download-beginner-blitz-cifar10-tutorial-py) to download the full example code.

# Training a Classifier[#](#training-a-classifier "Link to this heading")

Created On: Mar 24, 2017 | Last Updated: Sep 30, 2025 | Last Verified: Not Verified

This is it. You have seen how to define neural networks, compute loss and make updates to the weights of the network.

Now you might be thinking,

## What about data?[#](#what-about-data "Link to this heading")

Generally, when you have to deal with image, text, audio or video data, you can use standard python packages that load data into a numpy array. Then you can convert this array into a `torch.*Tensor`.

  * For images, packages such as Pillow, OpenCV are useful

  * For audio, packages such as scipy and librosa

  * For text, either raw Python or Cython based loading, or NLTK and SpaCy are useful

Specifically for vision, we have created a package called `torchvision`, that has data loaders for common datasets such as ImageNet, CIFAR10, MNIST, etc. and data transformers for images, viz., `torchvision.datasets` and `torch.utils.data.DataLoader`.

This provides a huge convenience and avoids writing boilerplate code.

For this tutorial, we will use the CIFAR10 dataset. It has the classes: ‘airplane’, ‘automobile’, ‘bird’, ‘cat’, ‘deer’, ‘dog’, ‘frog’, ‘horse’, ‘ship’, ‘truck’. The images in CIFAR-10 are of size 3x32x32, i.e. 3-channel color images of 32x32 pixels in size.

![cifar10](../../_images/cifar10.png)

cifar10[#](#id1 "Link to this image")

## Training an image classifier[#](#training-an-image-classifier "Link to this heading")

We will do the following steps in order:

  1. Load and normalize the CIFAR10 training and test datasets using `torchvision`

  2. Define a Convolutional Neural Network

  3. Define a loss function

  4. Train the network on the training data

  5. Test the network on the test data

### 1\. Load and normalize CIFAR10[#](#load-and-normalize-cifar10 "Link to this heading")

Using `torchvision`, it’s extremely easy to load CIFAR10.


    import torch
    import torchvision
    import torchvision.transforms as transforms


The output of torchvision datasets are PILImage images of range [0, 1]. We transform them to Tensors of normalized range [-1, 1].

Note

If you are running this tutorial on Windows or MacOS and encounter a BrokenPipeError or RuntimeError related to multiprocessing, try setting the num_worker of torch.utils.data.DataLoader() to 0.


    [transform](https://docs.pytorch.org/vision/stable/generated/torchvision.transforms.Compose.html#torchvision.transforms.Compose "torchvision.transforms.Compose") = [transforms.Compose](https://docs.pytorch.org/vision/stable/generated/torchvision.transforms.Compose.html#torchvision.transforms.Compose "torchvision.transforms.Compose")(
        [[transforms.ToTensor](https://docs.pytorch.org/vision/stable/generated/torchvision.transforms.ToTensor.html#torchvision.transforms.ToTensor "torchvision.transforms.ToTensor")(),
         [transforms.Normalize](https://docs.pytorch.org/vision/stable/generated/torchvision.transforms.Normalize.html#torchvision.transforms.Normalize "torchvision.transforms.Normalize")((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    batch_size = 4

    [trainset](https://docs.pytorch.org/vision/stable/generated/torchvision.datasets.CIFAR10.html#torchvision.datasets.CIFAR10 "torchvision.datasets.CIFAR10") = [torchvision.datasets.CIFAR10](https://docs.pytorch.org/vision/stable/generated/torchvision.datasets.CIFAR10.html#torchvision.datasets.CIFAR10 "torchvision.datasets.CIFAR10")(root='./data', train=True,
                                            download=True, [transform](https://docs.pytorch.org/vision/stable/generated/torchvision.transforms.Compose.html#torchvision.transforms.Compose "torchvision.transforms.Compose")=[transform](https://docs.pytorch.org/vision/stable/generated/torchvision.transforms.Compose.html#torchvision.transforms.Compose "torchvision.transforms.Compose"))
    trainloader = torch.utils.data.DataLoader([trainset](https://docs.pytorch.org/vision/stable/generated/torchvision.datasets.CIFAR10.html#torchvision.datasets.CIFAR10 "torchvision.datasets.CIFAR10"), batch_size=batch_size,
                                              shuffle=True, num_workers=2)

    [testset](https://docs.pytorch.org/vision/stable/generated/torchvision.datasets.CIFAR10.html#torchvision.datasets.CIFAR10 "torchvision.datasets.CIFAR10") = [torchvision.datasets.CIFAR10](https://docs.pytorch.org/vision/stable/generated/torchvision.datasets.CIFAR10.html#torchvision.datasets.CIFAR10 "torchvision.datasets.CIFAR10")(root='./data', train=False,
                                           download=True, [transform](https://docs.pytorch.org/vision/stable/generated/torchvision.transforms.Compose.html#torchvision.transforms.Compose "torchvision.transforms.Compose")=[transform](https://docs.pytorch.org/vision/stable/generated/torchvision.transforms.Compose.html#torchvision.transforms.Compose "torchvision.transforms.Compose"))
    testloader = torch.utils.data.DataLoader([testset](https://docs.pytorch.org/vision/stable/generated/torchvision.datasets.CIFAR10.html#torchvision.datasets.CIFAR10 "torchvision.datasets.CIFAR10"), batch_size=batch_size,
                                             shuffle=False, num_workers=2)

    classes = ('plane', 'car', 'bird', 'cat',
               'deer', 'dog', 'frog', 'horse', 'ship', 'truck')



      0%|          | 0.00/170M [00:00<?, ?B/s]
      0%|          | 459k/170M [00:00<00:37, 4.57MB/s]
      4%|▍         | 7.67M/170M [00:00<00:03, 44.2MB/s]
     11%|█         | 18.1M/170M [00:00<00:02, 71.6MB/s]
     17%|█▋        | 28.4M/170M [00:00<00:01, 84.0MB/s]
     22%|██▏       | 38.1M/170M [00:00<00:01, 88.4MB/s]
     28%|██▊       | 47.1M/170M [00:00<00:01, 89.1MB/s]
     33%|███▎      | 56.8M/170M [00:00<00:01, 91.4MB/s]
     39%|███▊      | 66.0M/170M [00:00<00:01, 91.7MB/s]
     45%|████▍     | 76.2M/170M [00:00<00:00, 94.8MB/s]
     50%|█████     | 85.7M/170M [00:01<00:00, 93.1MB/s]
     56%|█████▌    | 95.0M/170M [00:01<00:00, 92.7MB/s]
     61%|██████    | 104M/170M [00:01<00:00, 92.8MB/s]
     67%|██████▋   | 115M/170M [00:01<00:00, 95.4MB/s]
     73%|███████▎  | 124M/170M [00:01<00:00, 96.2MB/s]
     79%|███████▊  | 134M/170M [00:01<00:00, 96.8MB/s]
     85%|████████▍ | 144M/170M [00:01<00:00, 98.2MB/s]
     91%|█████████ | 155M/170M [00:01<00:00, 99.3MB/s]
     97%|█████████▋| 165M/170M [00:01<00:00, 99.9MB/s]
    100%|██████████| 170M/170M [00:01<00:00, 91.4MB/s]


Let us show some of the training images, for fun.


    import matplotlib.pyplot as plt
    import numpy as np

    # functions to show an image


    def imshow(img):
        img = img / 2 + 0.5     # unnormalize
        npimg = img.numpy()
        plt.imshow(np.transpose(npimg, (1, 2, 0)))
        plt.show()


    # get some random training images
    dataiter = iter(trainloader)
    images, labels = next(dataiter)

    # show images
    imshow([torchvision.utils.make_grid](https://docs.pytorch.org/vision/stable/generated/torchvision.utils.make_grid.html#torchvision.utils.make_grid "torchvision.utils.make_grid")(images))
    # print labels
    print(' '.join(f'{classes[labels[j]]:5s}' for j in range(batch_size)))


![cifar10 tutorial](../../_images/sphx_glr_cifar10_tutorial_001.png)


    car   frog  truck dog


### 2\. Define a Convolutional Neural Network[#](#define-a-convolutional-neural-network "Link to this heading")

Copy the neural network from the Neural Networks section before and modify it to take 3-channel images (instead of 1-channel images as it was defined).


    import torch.nn as nn
    import torch.nn.functional as F


    class Net(nn.Module):
        def __init__(self):
            super().__init__()
            self.conv1 = nn.Conv2d(3, 6, 5)
            self.pool = nn.MaxPool2d(2, 2)
            self.conv2 = nn.Conv2d(6, 16, 5)
            self.fc1 = nn.Linear(16 * 5 * 5, 120)
            self.fc2 = nn.Linear(120, 84)
            self.fc3 = nn.Linear(84, 10)

        def forward(self, x):
            x = self.pool(F.relu(self.conv1(x)))
            x = self.pool(F.relu(self.conv2(x)))
            x = torch.flatten(x, 1) # flatten all dimensions except batch
            x = F.relu(self.fc1(x))
            x = F.relu(self.fc2(x))
            x = self.fc3(x)
            return x


    net = Net()


### 3\. Define a Loss function and optimizer[#](#define-a-loss-function-and-optimizer "Link to this heading")

Let’s use a Classification Cross-Entropy loss and SGD with momentum.


    import torch.optim as optim

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)


### 4\. Train the network[#](#train-the-network "Link to this heading")

This is when things start to get interesting. We simply have to loop over our data iterator, and feed the inputs to the network and optimize.


    for epoch in range(2):  # loop over the dataset multiple times

        running_loss = 0.0
        for i, data in enumerate(trainloader, 0):
            # get the inputs; data is a list of [inputs, labels]
            inputs, labels = data

            # zero the parameter gradients
            optimizer.zero_grad()

            # forward + backward + optimize
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            # print statistics
            running_loss += loss.item()
            if i % 2000 == 1999:    # print every 2000 mini-batches
                print(f'[{epoch + 1}, {i + 1:5d}] loss: {running_loss / 2000:.3f}')
                running_loss = 0.0

    print('Finished Training')



    [1,  2000] loss: 2.205
    [1,  4000] loss: 1.827
    [1,  6000] loss: 1.666
    [1,  8000] loss: 1.552
    [1, 10000] loss: 1.511
    [1, 12000] loss: 1.479
    [2,  2000] loss: 1.406
    [2,  4000] loss: 1.391
    [2,  6000] loss: 1.379
    [2,  8000] loss: 1.324
    [2, 10000] loss: 1.332
    [2, 12000] loss: 1.297
    Finished Training


Let’s quickly save our trained model:


    PATH = './cifar_net.pth'
    torch.save(net.state_dict(), PATH)


See [here](https://pytorch.org/docs/stable/notes/serialization.html) for more details on saving PyTorch models.

### 5\. Test the network on the test data[#](#test-the-network-on-the-test-data "Link to this heading")

We have trained the network for 2 passes over the training dataset. But we need to check if the network has learnt anything at all.

We will check this by predicting the class label that the neural network outputs, and checking it against the ground-truth. If the prediction is correct, we add the sample to the list of correct predictions.

Okay, first step. Let us display an image from the test set to get familiar.


    dataiter = iter(testloader)
    images, labels = next(dataiter)

    # print images
    imshow([torchvision.utils.make_grid](https://docs.pytorch.org/vision/stable/generated/torchvision.utils.make_grid.html#torchvision.utils.make_grid "torchvision.utils.make_grid")(images))
    print('GroundTruth: ', ' '.join(f'{classes[labels[j]]:5s}' for j in range(4)))


![cifar10 tutorial](../../_images/sphx_glr_cifar10_tutorial_002.png)


    GroundTruth:  cat   ship  ship  plane


Next, let’s load back in our saved model (note: saving and re-loading the model wasn’t necessary here, we only did it to illustrate how to do so):


    net = Net()
    net.load_state_dict(torch.load(PATH, weights_only=True))



    <All keys matched successfully>


Okay, now let us see what the neural network thinks these examples above are:


    outputs = net(images)


The outputs are energies for the 10 classes. The higher the energy for a class, the more the network thinks that the image is of the particular class. So, let’s get the index of the highest energy:


    _, predicted = torch.max(outputs, 1)

    print('Predicted: ', ' '.join(f'{classes[predicted[j]]:5s}'
                                  for j in range(4)))



    Predicted:  cat   ship  plane plane


The results seem pretty good.

Let us look at how the network performs on the whole dataset.


    correct = 0
    total = 0
    # since we're not training, we don't need to calculate the gradients for our outputs
    with torch.no_grad():
        for data in testloader:
            images, labels = data
            # calculate outputs by running images through the network
            outputs = net(images)
            # the class with the highest energy is what we choose as prediction
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print(f'Accuracy of the network on the 10000 test images: {100 * correct // total} %')



    Accuracy of the network on the 10000 test images: 52 %


That looks way better than chance, which is 10% accuracy (randomly picking a class out of 10 classes). Seems like the network learnt something.

Hmmm, what are the classes that performed well, and the classes that did not perform well:


    # prepare to count predictions for each class
    correct_pred = {classname: 0 for classname in classes}
    total_pred = {classname: 0 for classname in classes}

    # again no gradients needed
    with torch.no_grad():
        for data in testloader:
            images, labels = data
            outputs = net(images)
            _, predictions = torch.max(outputs, 1)
            # collect the correct predictions for each class
            for label, prediction in zip(labels, predictions):
                if label == prediction:
                    correct_pred[classes[label]] += 1
                total_pred[classes[label]] += 1


    # print accuracy for each class
    for classname, correct_count in correct_pred.items():
        accuracy = 100 * float(correct_count) / total_pred[classname]
        print(f'Accuracy for class: {classname:5s} is {accuracy:.1f} %')



    Accuracy for class: plane is 71.4 %
    Accuracy for class: car   is 74.6 %
    Accuracy for class: bird  is 40.3 %
    Accuracy for class: cat   is 40.8 %
    Accuracy for class: deer  is 22.0 %
    Accuracy for class: dog   is 47.5 %
    Accuracy for class: frog  is 69.5 %
    Accuracy for class: horse is 59.3 %
    Accuracy for class: ship  is 57.0 %
    Accuracy for class: truck is 47.3 %


Okay, so what next?

How do we run these neural networks on the GPU?

## Training on GPU[#](#training-on-gpu "Link to this heading")

Just like how you transfer a Tensor onto the GPU, you transfer the neural net onto the GPU.

Let’s first define our device as the first visible cuda device if we have CUDA available:


    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

    # Assuming that we are on a CUDA machine, this should print a CUDA device:

    print(device)



    cuda:0


The rest of this section assumes that `device` is a CUDA device.

Then these methods will recursively go over all modules and convert their parameters and buffers to CUDA tensors:


    net.to(device)


Remember that you will have to send the inputs and targets at every step to the GPU too:


    inputs, labels = data[0].to(device), data[1].to(device)


Why don’t I notice MASSIVE speedup compared to CPU? Because your network is really small.

**Exercise:** Try increasing the width of your network (argument 2 of the first `nn.Conv2d`, and argument 1 of the second `nn.Conv2d` – they need to be the same number), see what kind of speedup you get.

**Goals achieved** :

  * Understanding PyTorch’s Tensor library and neural networks at a high level.

  * Train a small neural network to classify images

## Training on multiple GPUs[#](#training-on-multiple-gpus "Link to this heading")

If you want to see even more MASSIVE speedup using all of your GPUs, please check out [Optional: Data Parallelism](data_parallel_tutorial.html).

## Where do I go next?[#](#where-do-i-go-next "Link to this heading")

  * [Train neural nets to play video games](../../intermediate/reinforcement_q_learning.html)

  * [Train a state-of-the-art ResNet network on imagenet](https://github.com/pytorch/examples/tree/master/imagenet)

  * [Train a face generator using Generative Adversarial Networks](https://github.com/pytorch/examples/tree/master/dcgan)

  * [Train a word-level language model using Recurrent LSTM networks](https://github.com/pytorch/examples/tree/master/word_language_model)

  * [More examples](https://github.com/pytorch/examples)

  * [More tutorials](https://github.com/pytorch/tutorials)

  * [Discuss PyTorch on the Forums](https://discuss.pytorch.org/)

  * [Chat with other users on Slack](https://pytorch.slack.com/messages/beginner/)



    del dataiter


**Total running time of the script:** (1 minutes 26.418 seconds)

## Docs

Access comprehensive developer documentation for PyTorch

[View Docs](https://docs.pytorch.org/docs/stable/index.html)

## Tutorials

Get in-depth tutorials for beginners and advanced developers

[View Tutorials](https://docs.pytorch.org/tutorials)

## Resources

Find development resources and get your questions answered

[View Resources](https://pytorch.org/resources)

To analyze traffic and optimize your experience, we serve cookies on this site. By clicking or navigating, you agree to allow our usage of cookies. As the current maintainers of this site, Facebook’s Cookies Policy applies. Learn more, including about available controls: [Cookies Policy](https://opensource.fb.com/legal/cookie-policy).
