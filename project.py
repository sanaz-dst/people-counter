import cv2
face_cascade = cv2.CascadeClassifier('Sanaz_classifier.xml')
def get_face_bounding_box(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 6)
    return faces

def process_frame(frame):
    faces = get_face_bounding_box(frame)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, 'Number of People : {}'.format(len(faces)), (10, 100), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
    return frame


flag_source = False



if flag_source:
    cap = cv2.VideoCapture('film_Trim.mp4')
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
else:
    cap = cv2.VideoCapture(0)
    length = 100000

for i in range(length):
    ret, frame = cap.read()
    frame = process_frame(frame)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(33) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()