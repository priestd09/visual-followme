import argparse
import cv2

from fileUtils import getLoggers, closeloggers
from polyphemus import main


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Track a red blob and adjust camera gimbal to follow")
    parser.add_argument('-r', '--record', action="store_true", default=False, help='record the output of the program to ../vids/demo_X.avi')
    parser.add_argument('-i', '--input', action="store", help='use a video filename as an input instead of a webcam')
    args = parser.parse_args()
    
    video_in = cv2.VideoCapture()
    
    if args.input != None:
        video_in.open(args.input)
    else:
        video_in.open(0)
    
    if args.record:
        loggers = getLoggers()
    else:
        loggers = None  
    try:
        main(video_in, loggers)
    except KeyboardInterrupt:
        print "KeyboardInterrupt detected."
    cv2.destroyAllWindows()
    if args.record:
        closeloggers(loggers)
