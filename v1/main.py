import cv2
import time
from reasoning.describer import SceneDescriber
from speech.speaker import Narattor


def preprocess_for_blip(frame):
    frame = cv2.resize(frame, (384, 384))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return frame


def main():
    photo_mode = True  # Set to False for automatic mode

    cap = cv2.VideoCapture(0)
    speaker = Narattor()
    describer = SceneDescriber()
    last_caption = ""

    print("[INFO] Starting Blind AI...")
    if photo_mode:
        print("PHOTO MODE ENABLED — Press [SPACE] to capture, [Q] to quit.")

    last_time = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # === FPS Calculation ===
        current_time = time.time()
        delta = current_time - last_time
        fps = 1.0 / delta if delta > 0 else 0.0
        last_time = current_time

        # === Display FPS on Frame ===
        cv2.putText(frame, f"FPS: {fps:.1f}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # === Show Live Feed ===
        cv2.imshow("Blind AI - Press [SPACE] to describe | [Q] to quit", frame)
        key = cv2.waitKey(10) & 0xFF

        # === Handle Spacebar for Photo Mode ===
        if photo_mode and key == 32:  # Spacebar
            print("[INFO] Capturing frame...")
            processed_frame = preprocess_for_blip(frame)
            caption = describer.describe(processed_frame)

            weak_captions = {"a blurry image", "a photo", "a picture", "a room"}
            if caption not in weak_captions and caption != last_caption:
                print("[BLIP Caption]:", caption)
                speaker.speak(caption)
                last_caption = caption

        # === Quit on 'q' ===
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
