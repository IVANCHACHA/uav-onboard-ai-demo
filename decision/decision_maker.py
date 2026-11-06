class DecisionMaker:
    def make_decision(self, bbox, frame_width):
        if bbox is None:
            return None, None, None

        x, _, width, height = bbox
        bbox_area = width * height
        if bbox_area < 50_000:
            danger_level = "LOW"
        elif bbox_area < 75_000:
            danger_level = "MEDIUM"
        else:
            danger_level = "HIGH"

        center_x = x + width // 2
        if center_x < frame_width // 3:
            zone, command = "LEFT", "TURN_LEFT"
        elif center_x <= frame_width * 2 // 3:
            zone, command = "CENTER", "FORWARD"
        else:
            zone, command = "RIGHT", "TURN_RIGHT"

        if danger_level == "HIGH":
            command = "STOP"
        return danger_level, zone, command
