import cv2
import mediapipe as mp
import time

# ============================
# PARÂMETROS (pra explicar no vídeo)
# ============================
MIN_DETECTION_CONFIDENCE = 0.5   # teste 0.3 / 0.5 / 0.8 no vídeo
MODEL_SELECTION = 0              # 0 = rosto perto, 1 = rosto longe

mp_face = mp.solutions.face_detection
mp_draw = mp.solutions.drawing_utils

print("Abrindo camera com OpenCV (AVFOUNDATION)...")
cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)  # macOS

if not cap.isOpened():
    print("ERRO: nao foi possivel abrir a camera (indice 0).")
    print("Fecha Zoom/Meet/FaceTime/Photo Booth e confere permissoes de camera.")
    exit()

print("Camera aberta com sucesso!")

cap.set(3, 640)
cap.set(4, 480)

tempo_anterior = 0

with mp_face.FaceDetection(
    model_selection=MODEL_SELECTION,
    min_detection_confidence=MIN_DETECTION_CONFIDENCE
) as face_detector:

    while True:
        ret, frame = cap.read()

        if not ret:
            print("ret=False (falha ao ler frame). Tentando de novo...")
            time.sleep(0.05)
            continue

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape

        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = face_detector.process(img_rgb)

        num_faces = 0

        if result.detections:
            for det in result.detections:
                num_faces += 1
                mp_draw.draw_detection(frame, det)

                score = det.score[0]
                cv2.putText(
                    frame,
                    f"Usuario autenticado ({score:.2f})",
                    (10, 110),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),
                    2
                )
        else:
            cv2.putText(
                frame,
                "Nenhum rosto detectado",
                (10, 110),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 100, 255),
                2
            )

        # FPS
        tempo_atual = time.time()
        fps = 0
        if tempo_anterior != 0:
            fps = 1 / (tempo_atual - tempo_anterior)
        tempo_anterior = tempo_atual

        # Overlays
        cv2.putText(frame, f"Rostos: {num_faces}", (10, 25),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        cv2.putText(frame, f"FPS: {fps:.1f}", (10, 55),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 200, 200), 2)

        cv2.putText(frame,
                    f"min_conf={MIN_DETECTION_CONFIDENCE} | model={MODEL_SELECTION}",
                    (10, 85),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (180, 255, 180), 2)

        cv2.putText(frame, "Pressione 'q' para sair", (10, 470),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (180, 180, 180), 1)

        cv2.imshow("Camera + MediaPipe FaceDetection", frame)

        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
print("Encerrado.")
