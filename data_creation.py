import cv2
import os

folder_path = r"C:\Users\divyank.singhvi\Divyank\ctc_code\demo" 
image_files = [f for f in os.listdir(folder_path) if f.endswith((".png", ".jpg", ".jpeg"))]

drawing = False
rect_coords = {}
start_x, start_y = -1, -1

def draw_rectangle(event, x, y, flags, param):
    global image_with_rectangle, start_x, start_y, drawing, rect_coords

    image_with_rectangle = image.copy()

    cv2.putText(image_with_rectangle, f"({x}, {y})", (x + 10, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_x, start_y = x, y

    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        cv2.rectangle(image_with_rectangle, (start_x, start_y), (x, y), (0, 255, 0), 2)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        rect_coords = {"top_left": (start_x, start_y), "bottom_right": (x, y)}
        print("Rectangle Coordinates:", rect_coords)

cv2.namedWindow("Image Viewer")
cv2.setMouseCallback("Image Viewer", draw_rectangle)

for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)
    image = cv2.imread(image_path)

    if image is None:
        print(f"Could not open {image_file}, skipping...")
        continue

    image_with_rectangle = image.copy()

    while True:
        cv2.imshow("Image Viewer", image_with_rectangle)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to move to the next image
            break

cv2.destroyAllWindows()
