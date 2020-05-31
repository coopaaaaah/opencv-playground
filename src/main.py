import cv2
import time
import argparse


def record(letter):
    start_time = time.perf_counter()

    video = cv2.VideoCapture("http://192.168.1.112:8080/video")

    if not video.isOpened():
        print("Cannot open the video camera")
        return -1

    window_name = "My Webcam Feed"
    cv2.namedWindow(window_name)

    counter = 0
    while True:
        success, frame = video.read()

        if not success:
            print("Video camera is disconnected.")
            break

        cv2.imshow(window_name, frame)

        # saves every 10th frame to a png_file
        if counter % 10 == 0:
            cv2.imwrite('/Users/skehtch/Documents/ASL/' + str(letter) + '/' + str(counter) + '.png', frame)

        counter += 1

        # have we been recording for 10 seconds
        if time.perf_counter() - start_time > 7:
            print("Stopping the video.")
            break

    video.release()
    cv2.destroyAllWindows()

    return "done with " + str(letter)


parser = argparse.ArgumentParser(description='Record some letters.')
parser.add_argument('letter', type=str, nargs='+', help='a string for the recorder')
args = parser.parse_args()
record(args.letter[0])
