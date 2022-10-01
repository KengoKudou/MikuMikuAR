import cv2
import os


def imgload(imgdata):

    img = cv2.imread(imgdata)

    cv2.imshow("color", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    height, width, ch = img.shape
    size = width * height

    print("幅：", width)
    print("高さ：", height)
    print("チャンネル数:", ch)
    print("画素数:", size)
    print("データ型：", img.dtype)

    return img
