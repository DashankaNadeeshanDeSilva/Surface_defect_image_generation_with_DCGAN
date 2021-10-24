import cv2
import os


def rename_images(folder):
    print('running...')
    i = 0
    for filename in os.listdir(folder):
        image = cv2.imread(os.path.join(folder, filename))
        image64 = cv2.resize(image, (64, 64), interpolation=cv2.INTER_AREA)

        # For 'with defects' class, uncomment the below command
        #cv2.imwrite(f"ifpt_generated_renamed/with_defects.{i}.jpg", image64)

        # For 'without defects' class, uncomment the below command
        cv2.imwrite(f"ifpt_generated_renamed/without_defects.{i}.jpg", image64)

        i = i+1
    print('image saved')


if __name__ == '__main__':
    rename_images('temp/generated_images4')