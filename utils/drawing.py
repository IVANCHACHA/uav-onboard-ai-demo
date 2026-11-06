import cv2


class Drawer:
    def draw_hud(self, frame, bbox, status, frame_width):
        for border in (frame_width // 3, frame_width * 2 // 3):
            cv2.line(frame, (border, 0), (border, frame.shape[0]), (255, 255, 255), 2)

        if bbox is not None:
            x, y, width, height = bbox
            cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)
        if status is not None:
            cv2.putText(frame, status, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 0), 2)
        return frame
