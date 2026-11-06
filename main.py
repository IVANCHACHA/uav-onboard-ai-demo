import argparse

import cv2

from decision.decision_maker import DecisionMaker
from detectors.detector_colors import ColorDetector
from utils.drawing import Drawer


def main():
    parser = argparse.ArgumentParser(description="Демонстрация компьютерного зрения для БПЛА")
    parser.add_argument("--source", default="0", help="Номер камеры или путь к видео")
    parser.add_argument("--detector", choices=("yolo", "color"), default="yolo")
    args = parser.parse_args()

    if args.detector == "yolo":
        from detectors.yolo_detectors import YoloDetector

        detector = YoloDetector()
    else:
        detector = ColorDetector()

    source = int(args.source) if args.source.isdecimal() else args.source
    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        raise SystemExit("Не удалось открыть камеру или видео")

    decision = DecisionMaker()
    drawing = Drawer()
    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break

            frame_width = frame.shape[1]
            bbox, _, debug_frame = detector.detect(frame)
            danger_level, zone, command = decision.make_decision(bbox, frame_width)
            status = f"{danger_level} / {zone} / {command}" if bbox is not None else None
            hud_frame = drawing.draw_hud(frame.copy(), bbox, status, frame_width)
            cv2.imshow("Detection", debug_frame)
            cv2.imshow("Camera HUD", hud_frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
