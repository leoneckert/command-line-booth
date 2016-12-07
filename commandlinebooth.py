import numpy as np
import cv2
import time
import curses

def cinema(window):
    cap = cv2.VideoCapture(0)
    while(True):

        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized_image = cv2.resize(gray, (0,0), fx=0.04, fy=0.04)

        string = ""
        for row in range(resized_image.shape[0]):
            for column in range(resized_image.shape[1]):
                if (resized_image[row][column] < 30): string += "WW"
                elif(resized_image[row][column] < 60): string += "ww"
                elif(resized_image[row][column] < 90): string += "ll"
                elif(resized_image[row][column] < 120): string += "ii"
                elif(resized_image[row][column] < 150): string += "::"
                elif(resized_image[row][column] < 180): string += ",,"
                elif(resized_image[row][column] < 220): string += ".."
                else: string += "  "
            string += "\n"

        window.addstr(0, 0, string)
        window.refresh()
        time.sleep(0.1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

curses.wrapper(cinema)
