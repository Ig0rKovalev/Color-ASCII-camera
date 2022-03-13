import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np


DENSITY = ' .",:;!~+-cba*#W&8@'
LEN_DENSITY = 255 / len(DENSITY)


def drow(img, height, width):
    img_new = Image.new("RGBA", (height, width), 'black')

    draw = ImageDraw.Draw(img_new)
    font = ImageFont.truetype("courier.ttf", 10)

    for i in range(0, width, 5):
        for j in range(0, height, 5):
            b, g, r = img[i, j]
            pixelIndex = int(((b + g + r) // 3) // LEN_DENSITY)
            if (((b + g + r) // 3) % LEN_DENSITY) == 0 and pixelIndex != 0:
                draw.text((j, i), DENSITY[pixelIndex], fill=(r, g, b), font=font)
            else:
                draw.text((j, i), DENSITY[pixelIndex + 1], fill=(r, g, b), font=font)

    cv2_im_processed = cv2.cvtColor(np.array(img_new), cv2.COLOR_RGB2BGR)
    cv2.imshow("main", cv2_im_processed)


def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, img = cap.read()
        img = cv2.resize(img, (600, 600), interpolation=cv2.INTER_NEAREST)
        drow(img, 600, 600)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return


if __name__ == "__main__":
    main()
