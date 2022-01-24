from google.colab import files
import os

def upload_file(filename=None):
    """ Upload a file in google colaboratory
    :type filename: string
    :param filename: Path where to save the uploaded file (None to keep the default location)

    :rtype: string
    :return: the location of the uploaded file
    """
    uploaded = files.upload()
    upload_name = list(uploaded.keys())[0]

    if not filename is None:
        os.system("rm -rf " + filename)
        os.system("mv " + upload_name + " " + filename)
        return filename

    return upload_name


    
