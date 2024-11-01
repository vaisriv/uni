import cv2 as cv
import matplotlib.pyplot as plt

flags = [i for i in dir(cv) if i.startswith("COLOR_")]
print(len(flags), "flags total:")

print(flags[48])

path = "./test_images/tiger_images/tiger"

tiger_friends = []
for i in range(1, 6):
    friend = cv.cvtColor(cv.imread(path + str(i) + ".jpeg"), cv.COLOR_BGR2RGB)
    tiger_friends.append(friend)

# TODO: Update colors with hsv plot values of each img
highlights = [(30, 62.7, 56.9), (33, 68, 98), (34, 73, 91), (32, 57, 68), (77, 3, 92)]
shadows = [(30, 58, 24), (16, 94, 35), (31, 90, 12), (29, 93, 35), (58, 20, 48)]


def segment_tiger(image, highlight, shadow):
    """Attempts to segment the tiger out of the provided image."""
    hsv_image = cv.cvtColor(image, cv.COLOR_RGB2HSV)
    mask = cv.inRange(hsv_image, highlight, shadow)
    result = cv.bitwise_and(image, image, mask=mask)
    result = cv.GaussianBlur(result, (7, 7), 0)
    return result


results = [
    segment_tiger(tiger_friends[i], highlight=highlights[i], shadow=shadows[i])
    for i in range(len(tiger_friends))
]

for i in range(5):
    plt.subplot(1, 2, 1)
    plt.imshow(tiger_friends[i])
    plt.subplot(1, 2, 2)
    plt.imshow(results[i])
    plt.show()
