from cv2 import (cvtColor, COLOR_RGB2BGR, imshow, VideoCapture,
                 waitKey, INTER_NEAREST, resize)
from PIL import ImageFont, ImageDraw, Image
from numpy import array
from os.path import dirname, abspath


DENSITY = ' .",:;!~+-cba*#W&8@'
LEN_DENSITY = 256 / len(DENSITY)
FONT = ImageFont.truetype(dirname(abspath(__file__)) + "\courier.ttf", size=9)


def drow(img):
    img_new = Image.new("RGBA", (600, 600), 'black')
    draw = ImageDraw.Draw(img_new)

    for i in range(0, 601, 7):
        for j in range(0, 601, 7):
            b, g, r = img[i, j]
            b = int(b)
            g = int(g)
            r = int(r)
            pixelIndex = int(((b + g + r) // 3) // LEN_DENSITY)
            if int((((b + g + r) // 3) % LEN_DENSITY)) == 0 and pixelIndex != 0:
                draw.text((j, i), DENSITY[pixelIndex-1], fill=(r, g, b), font=FONT)
            else:
                draw.text((j, i), DENSITY[pixelIndex], fill=(r, g, b), font=FONT)

    cv2_im_processed = cvtColor(array(img_new), COLOR_RGB2BGR)
    imshow("ASCII Video", cv2_im_processed)


def main():
    cap = VideoCapture(0)

    while True:
        ret, img = cap.read()
        img = resize(img, (600, 600), interpolation=INTER_NEAREST)
        drow(img)
        if waitKey(1) & 0xFF == ord('q'):
            return


if __name__ == "__main__":
    main()
