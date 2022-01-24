import cv2 
import matplotlib.pyplot as plt 
import numpy as np

def read_image(filename, grayscale=False, resize=None, plot=True, rescale_intensity=True):
    """ Read an image file from its path
    :type filename: string
    :param filename: path to the image to be read

    :type grayscale: boolean
    :param grayscale: load image in grayscale?

    :type resize: pair
    :param resize: resizes the image to this resolution (None to do no resizing)

    :type plot: boolean
    :param plot: if True, plots this image

    :type rescale_intensity: Boolean
    :param rescale_intensity: If true, rescales pixel color channels by dividing for 255.0

    :rtype: an image (numpy vector)
    """
    # read image 
    if grayscale:
        img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    else:
        img = cv2.imread(filename)
    # resize
    if not resize is None:
        img = cv2.resize(img, dsize=resize, interpolation=cv2.INTER_CUBIC)
    
    # rescale intensity
    if rescale_intensity:
        img = 1 - (img / 255.0)

    # draw image
    if plot:
        plt.imshow(img)
    
    return img


def categorize(model, categories, element, true_label=""):
    """ Plot an image and the probabilities of the possible categories
    :type model: NN
    :param model: a neural network model, retunring a probability vector

    :type categories: [string]
    :param categories: names for the categories

    :type element: numpy tensor
    :param element: the input for the NN

    :type true_label: string
    :param true_label: the true label, if known
    """
    output = model(np.array([element])).numpy().reshape((len(categories), ))
    prediction = categories[np.argmax(output)]

    # plot the image
    plt.figure(figsize=(6,3))
    plt.subplot(1,2,1)

    plt.imshow(element, cmap=plt.cm.get_cmap("gray"))
    plt.xlabel("{} {:2.0f}% ({})".format(prediction,
                                100*np.max(output),
                                true_label))

    # plot the barplot
    plt.subplot(1,2,2)

    barplot = plt.bar(range(len(categories)), output, color="#777777")
    plt.xticks(range(len(categories)), categories, rotation=90)

    plt.ylim([0, 1])

    barplot[np.argmax(output)].set_color('red')

    plt.show()