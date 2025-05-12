# Vai Srivastava - 0106

# imports
import cv2 as cv
import matplotlib.pyplot as plt

def segment_tiger(image, highlight, shadow):
    """Attempts to segment the tiger out of the provided image."""
    blur = cv.blur(image, (5, 5))  # apply blur to reduce noise
    hsv_image = cv.cvtColor(blur, cv.COLOR_RGB2HSV)  # convert to HSV color space
    mask = cv.inRange(hsv_image, shadow, highlight)  # create mask within shadow/highlight range
    result = cv.bitwise_and(image, image, mask=mask)  # apply mask to isolate target region
    result = cv.GaussianBlur(result, (7, 7), 0)  # apply Gaussian blur to smooth output
    return result  # return segmented image

if __name__ == "__main__":
    # list all color conversion flags in OpenCV
    flags = [i for i in dir(cv) if i.startswith("COLOR_")]
    print(len(flags), "flags total:")  # print number of flags
    print(flags[48])  # print a sample flag for reference

    path = "./test_images/tiger_images/tiger"  # base path to tiger images

    tiger_friends = []  # list to store tiger images
    for i in range(1, 6):  # loop to load each tiger image
        friend = cv.cvtColor(cv.imread(path + str(i) + ".jpeg"), cv.COLOR_BGR2RGB)  # read and convert image
        tiger_friends.append(friend)  # add image to list

    # define highlight and shadow ranges for each tiger image
    highlights_hsv = [
        (20, 255, 255),
        (17.5, 255, 255),
        (20, 255, 255),
        (20, 255, 255),
        (45, 255, 255),
    ]
    shadows_hsv = [
        (0, 0, 0),
        (10, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),
    ]

    # segment each tiger image using the defined highlight/shadow ranges
    results = [
        segment_tiger(
            tiger_friends[i], highlight=highlights_hsv[i], shadow=shadows_hsv[i]
        )
        for i in range(len(tiger_friends))
    ]

    # display each original and segmented image pair
    for i in range(5):
        plt.subplot(1, 2, 1)  # setup subplot for original image
        plt.imshow(tiger_friends[i])  # show original image
        plt.subplot(1, 2, 2)  # setup subplot for segmented result
        plt.imshow(results[i])  # show segmented image
        plt.show()  # display the figure
