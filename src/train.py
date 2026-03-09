import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from ultralytics import YOLO


def main():

    # last checkpoint load karo
    model = YOLO("runs/detect/train10/weights/last.pt")

    model.train(
        data="fire_dataset.yaml",
        resume=True
    )


if __name__ == "__main__":
    main()