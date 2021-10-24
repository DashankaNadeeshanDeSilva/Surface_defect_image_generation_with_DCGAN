import cv2
import os


def split_images(folder):
    print('running...')
    for filename in os.listdir(folder):
        image = cv2.imread(os.path.join(folder, filename))

        # resize image 4096 x 256
        d_size = (4096, 256)
        img = cv2.resize(image, d_size, interpolation=cv2.INTER_AREA)

        # image naming
        split_string = filename.split(".", 1)
        filename = split_string[0]

        # slice images
        if img is not None:
            for r in range(0, img.shape[0], 64):
                for c in range(0, img.shape[1], 64):
                    #print(filename)
                    cv2.imwrite(f"split_data/train/img_{filename}_{r}_{c}.jpg", img[r:r + 64, c:c + 64, :])
    print('done !')


if __name__ == '__main__':
    
    data_dir = 'Raw Dataset2'
    split_images(data_dir)
