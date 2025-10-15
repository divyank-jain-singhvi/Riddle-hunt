from ultralytics import YOLO
import cv2

# Load the trained model
model = YOLO(r"C:\Users\divyank.singhvi\Divyank\ctc_code\runs\detect\train7\weights\best.pt")  # Adjust path if needed
# Run inference
results = model.predict(source=r"C:\Users\divyank.singhvi\Divyank\ctc_code\demo\train\images\page_11.jpg",conf=0.02,imgsz=960)

# Print detected objects
for result in results:
    img = result.plot(line_width=1, font_size=1) 
    cv2.imshow("Detected Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

