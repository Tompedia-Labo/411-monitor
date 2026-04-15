import cv2

def draw_boxes(frame, boxes):
    """バウンディングボックス描画"""
    for x1, y1, x2, y2 in boxes:
        cv2.rectangle(frame, (x1,y1), (x2,y2), (255,0,0), 2)
    return frame
