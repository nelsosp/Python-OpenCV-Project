import cv2
import numpy as np


def detect_lane_lines(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to the grayscale image
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Apply Canny edge detection
    edges = cv2.Canny(blurred_image, 50, 150)

    # Define the region of interest (ROI) for lane detection
    height, width = edges.shape
    vertices = np.array(
        [[(0, height), (width // 2, height // 2), (width, height)]], dtype=np.int32)
    masked_edges = region_of_interest(edges, vertices)

    # Apply Hough Line Transform to detect lane lines
    lines = cv2.HoughLinesP(masked_edges, rho=1, theta=np.pi /
                            180, threshold=40, minLineLength=100, maxLineGap=5)

    # Draw the detected lines on the original image
    line_image = np.copy(image) * 0  # Create a blank image to draw lines
    draw_lines(line_image, lines)

    # Combine the line image with the original image
    result = cv2.addWeighted(image, 0.8, line_image, 1, 0)

    return result


def region_of_interest(edges, vertices):
    mask = np.zeros_like(edges)
    cv2.fillPoly(mask, vertices, 255)
    masked_edges = cv2.bitwise_and(edges, mask)
    return masked_edges


def draw_lines(image, lines, color=(0, 255, 0), thickness=5):
    if lines is None:
        return

    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), color, thickness)


def main():
    # Open the video file
    # Replace this with the path to your video file
    video_path = "videos/road2.mp4"
    cap = cv2.VideoCapture(video_path)

    # Check if the video file was opened successfully
    if not cap.isOpened():
        print("Error: Video file not found or invalid format.")
        return

    # Define the desired medium size for the video frames
    desired_width = 640
    desired_height = 480

    while True:
        # Read a frame from the video
        ret, frame = cap.read()

        # If the frame was not read successfully, the video has ended
        if not ret:
            break

        # Resize the frame to the desired medium size
        resized_frame = cv2.resize(frame, (desired_width, desired_height))

        # Detect and draw lane lines
        lane_detected_frame = detect_lane_lines(resized_frame)

        # Display the frame with lane lines
        cv2.imshow("Lane Detection", lane_detected_frame)

        # Wait for a key press and exit the loop if 'q' is pressed
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Release the video capture object and close the display window
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()


# live video capture------------------------------------------------------------------------------------------------------------


# import cv2
# import numpy as np


# def detect_lane_lines(image):
#     # Convert the image to grayscale
#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Apply Gaussian blur to the grayscale image
#     blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

#     # Apply Canny edge detection
#     edges = cv2.Canny(blurred_image, 50, 150)

#     # Define the region of interest (ROI) for lane detection
#     height, width = edges.shape
#     vertices = np.array(
#         [[(0, height), (width // 2, height // 2), (width, height)]], dtype=np.int32)
#     masked_edges = region_of_interest(edges, vertices)

#     # Apply Hough Line Transform to detect lane lines
#     lines = cv2.HoughLinesP(masked_edges, rho=1, theta=np.pi /
#                             180, threshold=40, minLineLength=100, maxLineGap=5)

#     # Draw the detected lines on the original image
#     line_image = np.copy(image) * 0  # Create a blank image to draw lines
#     draw_lines(line_image, lines)

#     # Combine the line image with the original image
#     result = cv2.addWeighted(image, 0.8, line_image, 1, 0)

#     return result


# def region_of_interest(edges, vertices):
#     mask = np.zeros_like(edges)
#     cv2.fillPoly(mask, vertices, 255)
#     masked_edges = cv2.bitwise_and(edges, mask)
#     return masked_edges


# def draw_lines(image, lines, color=(0, 255, 0), thickness=5):
#     if lines is None:
#         return

#     for line in lines:
#         x1, y1, x2, y2 = line[0]
#         cv2.line(image, (x1, y1), (x2, y2), color, thickness)


# def main():
#     # Open the video camera
#     # 0 represents the default camera, change it to a different number if you have multiple cameras
#     cap = cv2.VideoCapture(0)

#     # Check if the camera was opened successfully
#     if not cap.isOpened():
#         print("Error: Unable to access the camera.")
#         return

#     # Define the desired medium size for the video frames
#     desired_width = 640
#     desired_height = 480

#     while True:
#         # Read a frame from the camera
#         ret, frame = cap.read()

#         # If the frame was not read successfully, break the loop
#         if not ret:
#             break

#         # Resize the frame to the desired medium size
#         resized_frame = cv2.resize(frame, (desired_width, desired_height))

#         # Detect and draw lane lines
#         lane_detected_frame = detect_lane_lines(resized_frame)

#         # Display the frame with lane lines
#         cv2.imshow("Lane Detection", lane_detected_frame)

#         # Wait for a key press and exit the loop if 'q' is pressed
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Release the video capture object and close the display window
#     cap.release()
#     cv2.destroyAllWindows()


# if __name__ == "__main__":
#     main()


# live video capture to specify target of another webcam/camera---------------------------------------------------------------------------------------------


# def main():
#     # Open the high-definition camera (change the index to the correct one)
#     cap = cv2.VideoCapture(1)  # Use the correct camera index (e.g., 1)

#     # Check if the camera was opened successfully
#     if not cap.isOpened():
#         print("Error: Unable to access the camera.")
#         return

#     # Set the desired resolution for the camera (change to your desired resolution)
#     desired_width = 1280
#     desired_height = 720
#     cap.set(cv2.CAP_PROP_FRAME_WIDTH, desired_width)
#     cap.set(cv2.CAP_PROP_FRAME_HEIGHT, desired_height)

#     while True:
#         # Read a frame from the camera
#         ret, frame = cap.read()

#         # If the frame was not read successfully, break the loop
#         if not ret:
#             break

#         # Detect and draw lane lines
#         lane_detected_frame = detect_lane_lines(frame)

#         # Display the frame with lane lines
#         cv2.imshow("Lane Detection", lane_detected_frame)

#         # Wait for a key press and exit the loop if 'q' is pressed
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Release the video capture object and close the display window
#     cap.release()
#     cv2.destroyAllWindows()
