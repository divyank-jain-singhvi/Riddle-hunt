import cv2
import os

folder_path = r"demo\images"
image_files = [f for f in os.listdir(folder_path) if f.endswith((".png", ".jpg", ".jpeg"))]
data={'current_file':None}
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
        center_x,center_y=(x-start_x)/2,(y-start_y)/2
        center=[(start_x+center_x)/1116,(start_y+center_y)/722]
        print(center)
        width,height=(x-start_x)/1116,(y-start_y)/722
        print(height,width)
        try:
            for i in range(5):
                class_id=int(input('enter class ID'))
                if class_id != 999:
                    class_name=input('enter class Name')
                    label_exist_flag=True
                    with open(rf"demo\labels\{param['current_file'].split('.')[0]}.txt", "a") as file:
                        file.write(f"{class_id} {center[0]} {center[1]} {width} {height}\n")
                        print("label added successfully!")
                    with open(r"demo\label_data.txt", 'r') as file1:
                        lines = file1.readlines()
                        for line in lines:
                            if class_name in line or str(class_id) in line:
                                label_exist_flag = False
                                print("class exist new class not added")
                                break
                    if label_exist_flag:
                        with open(r"demo\label_data.txt", 'a') as file1:
                            file1.write(f"{class_id} {class_name}\n")
                            print("class added")
                else:
                    print("cancled...")
                break
        except Exception as e:
            print(e)
            print(f"attempt {i} try again...!")


cv2.namedWindow("Image Viewer")
cv2.setMouseCallback("Image Viewer", draw_rectangle,data)

for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)
    image = cv2.imread(image_path)
    data['current_file']=image_file

    if image is None:
        print(f"Could not open {image_file}, skipping...")
        continue

    image_with_rectangle = image.copy()

    while True:
        cv2.imshow("Image Viewer", image_with_rectangle)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()
