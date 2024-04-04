from matplotlib import pyplot as plt
import cv2
import numpy as np

# Load image
file_path = 'C:/Users/Sajid/Desktop/Codes/fish egg count/11.jpeg'
image = cv2.imread(file_path)

# Convert to gray scale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use Gaussian blur
blurred_image = cv2.GaussianBlur(gray_image, (9, 9), 0)

# Apply Hough transform on the blurred image.
detected_circles = cv2.HoughCircles(
    blurred_image,
    cv2.HOUGH_GRADIENT,
    dp=1.3,
    minDist=10,
    param1=70,
    param2=15,
    minRadius=1,
    maxRadius=10
)
count = 0;
# Draw circles that are detected.
if detected_circles is not None:
    # Convert the circle parameters a, b and r to integers.
    detected_circles_rounded = np.uint16(np.around(detected_circles))

    count = 0  # to count the eggs
    for pt in detected_circles_rounded[0, :]:
        a, b, r = pt[0], pt[1], pt[2]

        # Draw the circumference of the circle.
        cv2.circle(image, (a, b), r, (0, 255, 0), 2)

        # Draw a small circle (of radius 1) to show the center.
        cv2.circle(image, (a, b), 1, (0, 0, 255), 3)
        count += 1

# Save the output image with circles
output_path = 'C:/Users/Sajid/Desktop/Codes/fish egg count/11_count2.jpg'
cv2.imwrite(output_path, image)

# Display the result and count
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title(f'Number of Eggs: {count}')
plt.show()

output_path, count
