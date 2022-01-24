import cv2 
import matplotlib.pyplot as plt 
  
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

