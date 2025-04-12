import cv2
from detectors.yolo_detector import YOLOv11Detector
from captioning.blip_captioner import BLIPCaptioner
from language.llama_client import LLaMAClient
from speech.speaker import Narrator

def main():
    cap = cv2.VideoCapture(0)
    yolo = YOLOv11Detector()
    blip = BLIPCaptioner()
    llama = LLaMAClient()
    speaker = Narrator()

    print("[INFO] Blind AI running — press [SPACE] to describe scene, [Q] to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Blind AI - Press [SPACE] to describe | [Q] to quit", frame)
        key = cv2.waitKey(10) & 0xFF

        if key == ord('q'):
            break

        if key == 32:  # Spacebar
            print("[INFO] Detecting + captioning...")
            objects = yolo.detect_objects(frame)
            blip_caption = blip.caption(frame)

            weak_blips = ["a blurry", "a photo", "a picture", "a person", "someone", "nothing"]
            if any(phrase in blip_caption.lower() for phrase in weak_blips):
                print("[BLIP]: weak caption, ignored.")
                blip_caption = ""

            print("[YOLO]:", objects)
            print("[BLIP]:", blip_caption)

            if not objects:
                speaker.speak("Sorry, I couldn't detect anything in the scene.")
                return

            description = llama.generate_description(objects, blip_caption)
            print("[LLaMA]:", description)
            speaker.speak(description)


    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
