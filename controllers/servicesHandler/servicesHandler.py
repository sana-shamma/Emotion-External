from fer import FER
import cv2
from inference.core.interfaces.camera.entities import VideoFrame
from inference import InferencePipeline
from datetime import datetime


class ServicesHandler:
    def __init__(self):
        self.results = []  # Store results in a list

    def my_custom_sink(self, predictions: dict, video_frame: VideoFrame):
        labels_confidence = [(p["class"], p["confidence"]) for p in predictions["predictions"]]
        if labels_confidence:
            for id, label_confidence in enumerate(labels_confidence):
                emotion_result = label_confidence[0]
                emotion_score = label_confidence[1]
                face_id = id
                self.results.append((face_id, emotion_result, emotion_score))

    def handle_emotion_predict(self, camera_url):
        pipeline = InferencePipeline.init(
            model_id="emotion-detection-cwq4g/1",
            api_key="CL44RJt0AHwiczZPxMLN",
            video_reference=camera_url,
            on_prediction=lambda predictions, video_frame: self.my_custom_sink(predictions, video_frame),
        )
        pipeline.start()
        pipeline.join()

   