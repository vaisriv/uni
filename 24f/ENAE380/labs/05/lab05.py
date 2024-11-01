# Vai Srivastava - 0106
"""
This is your template for lab5. Implement all questions in the appropriate
function. You are encouraged to implement helper functions as needed with
a short (one-line) description of their purpose.
"""

# imports
import cv2 as cv
import time
import numpy as np


class Lab5:

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
        img = cv.imread(filePath)  # read image from file
        sum_blue = int(np.sum(img[:, :, 0]))  # sum all blue values
        sum_green = int(np.sum(img[:, :, 1]))  # sum all green values
        sum_red = int(np.sum(img[:, :, 2]))  # sum all red values
        return (sum_blue, sum_green, sum_red)  # return sums as tuple

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
        return np.argmax(
            self.calculate_spectrum(filePath)
        )  # get index of highest color sum

    def measure_runtime_numpy(self):
        """
        Measures the time it takes to run timing_numpy() on 'test_image.png'

        Returns
        -------
        float
            time taken to run timing_numpy
        """
        starttime = time.time()  # start timer
        self.timing_numpy("./test_images/test_image.png")  # run numpy timing
        endtime = time.time()  # stop timer
        return endtime - starttime  # return elapsed time

    def measure_runtime_python(self):
        """
        Calculates the time it takes to run timing_python() on 'test_image.png'

        Returns
        -------
        float
            time taken to run timing_python
        """
        starttime = time.time()  # start timer
        self.timing_python("./test_images/test_image.png")  # run python timing
        endtime = time.time()  # stop timer
        return endtime - starttime  # return elapsed time

    def timing_numpy(self, filePath):
        """Accesses each pixel of an image via numpy. Do not modify this function."""
        IMG = cv.imread(filePath)
        info = IMG.shape
        for row in range(0, info[0]):
            for col in range(0, info[1]):
                Blue_pixel = IMG.item(row, col, 0)
                Green_pixel = IMG.item(row, col, 1)
                Red_pixel = IMG.item(row, col, 2)

    def timing_python(self, filePath):
        """Accesses each pixel of an image via python lists. Do not modify this function."""
        IMG = cv.imread(filePath)
        info = IMG.shape
        for row in range(0, info[0]):
            for col in range(0, info[1]):
                Blue_pixel = IMG[row][col][0]
                Green_pixel = IMG[row][col][1]
                Red_pixel = IMG[row][col][2]

    def blur_image(self, infilePath, outfilePath):
        """
        Blurs the input image using a Gaussian filter.
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
        inimg = cv.imread(infilePath)  # read input image
        outimg = cv.GaussianBlur(inimg, (5, 5), 0)  # apply gaussian blur
        cv.imwrite(outfilePath, outimg)  # save blurred image
        return outimg  # return blurred image

    def findoutlines(self, infilePath, outfilePath):
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
        inimg = cv.imread(infilePath)  # read input image

        gray = cv.cvtColor(inimg, cv.COLOR_BGR2GRAY)  # convert to grayscale
        _, thresh = cv.threshold(
            gray, 1, 255, cv.THRESH_BINARY + cv.THRESH_OTSU
        )  # binarize
        contours, _ = cv.findContours(
            thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE
        )  # find contours

        outimg = inimg  # copy original for drawing
        cv.drawContours(outimg, contours, -1, (255, 255, 255), 2)  # draw white contours
        cv.imwrite(outfilePath, outimg)  # save outlined image
        return outimg  # return outlined image


if __name__ == "__main__":
    lab = Lab5()  # create Lab5 instance
    # print color intensities for test image
    print("test_img spectrum:", lab.calculate_spectrum("./test_images/test_image.png"))
    # print dominant color index for test image
    print("test_img max: index", lab.get_dominant_color("./test_images/test_image.png"))
    # measure and print numpy runtime
    print("numpy:", lab.measure_runtime_numpy(), "seconds")
    # measure and print python runtime
    print("python:", lab.measure_runtime_numpy(), "seconds")
    # display blurred image result
    cv.imshow(
        "blur test:",
        lab.blur_image("./test_images/BlurMe.png", "./test_images/Srivastava_2a.png"),
    )
    cv.waitKey(0)
    # display outlined image result
    cv.imshow(
        "outline test:",
        lab.findoutlines(
            "./test_images/BlueSquare.png", "./test_images/Srivastava_2b.png"
        ),
    )
    cv.waitKey(0)
    cv.destroyAllWindows()  # close all windows
