# Vai Srivastava - 0106
"""
This is your template for lab5. Implement all questions in the appropriate
function. You are encouraged to implement helper functions as needed with
a short (one-line) description of their purpose.
"""

import cv2
import time

class Lab5():

    def calculate_spectrum(self, filePath):
        """
        Reports the total intensity of each of the three colors of an image

        Parameters
        ----------
        filePath : str
            path to original image file

        Returns
        -------
        result : (int, int, int)
            total intesities in each of the BGR color channels respectively

        """


    def get_dominant_color(self, filePath):
        """
        Outputs the most dominant color of an image

        Parameters
        ----------
        filePath : str
            path to original image file, stored as a string

        Returns
        -------
        int
            0 for Blue, 1 for Green, 2 for Red

        """


    def measure_runtime_numpy(self):
        """
        Measures the time it takes to run timing_numpy() on 'test_image.png'

        Returns
        -------
        float
            time taken to run timing_numpy
        """


    def measure_runtime_python(self):
        """
        Calculates the time it takes to run timing_python() on on 'test_image.png'

        Returns
        -------
        float
            time taken to run timing_python

        """


    def timing_numpy(self, filePath):
        """ Accesses each pixel of an image via numpy. Do not modify this function. """
        IMG=cv2.imread(filePath)
        info=IMG.shape
        for row in range(0,info[0]):
            for col in range(0,info[1]):
                Blue_pixel=IMG.item(row,col,0)
                Green_pixel=IMG.item(row,col,1)
                Red_pixel=IMG.item(row,col,2)


    def timing_python(self, filePath):
        """ Accesses each pixel of an image via python lists. Do not modify this function. """
        IMG=cv2.imread(filePath)
        info=IMG.shape
        for row in range(0,info[0]):
            for col in range(0,info[1]):
                Blue_pixel=IMG[row][col][0]
                Green_pixel=IMG[row][col][1]
                Red_pixel=IMG[row][col][2]



    def blur_image(self, filePath):
        """
        Blurs the input image using a Guassian filter.
        Note that the function takes a file path, not a loaded image, as input,
        per the Piazza discussion.

        Parameters
        ----------
        filePath : str
            path to original image file

        Returns
        -------
        numpy.ndarray
            the newly generated image

        """



    def findoutlines(self, filePath):
        """
        Outputs and writes an image outlining the shapes contained in the input image

        Parameters
        ----------
        filePath : str
            path to original image file

        Returns
        -------
        numpy.ndarray
            the newly generated image
        """

'''
if __name__ == '__main__':
    l = Lab5()
    b = l.findoutlines('files/BlueSquare.png')
    print(b)
'''
