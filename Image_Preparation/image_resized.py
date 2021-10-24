
import cv2
import os

def remove_black_images(folder):
    print('running...')

    for filename in os.listdir(folder):
        image = cv2.imread(os.path.join(folder, filename))
        image64 = cv2.resize(image, (64, 64), interpolation=cv2.INTER_AREA)


        # cv2.imwrite(f"cleaned_data_64x64_14/without/{filename}.jpg", image64)
        cv2.imwrite(f"results/{filename}.jpg", image64)
    print('image saved')


remove_black_images('temp')