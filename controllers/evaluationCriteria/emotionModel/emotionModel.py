from ..detectionModelAdaptor.detectionModelAdaptor import DetectionModelAdaptor
from ...servicesHandler.servicesHandler import ServicesHandler
import cv2
from fer import FER
import threading

class EmotionModel(DetectionModelAdaptor):

    def __init__(self):
        self.__services_handler = ServicesHandler()
        self.results = [] 


    def predict_emotion(self,camera_url):
        self.__services_handler.handle_emotion_predict(camera_url)

    def process_results(self):
        while True:
            if self.__services_handler.results:
                face_id, emotion_result, emotion_score = self.__services_handler.results.pop(0)
                self.results.append((face_id, emotion_result, emotion_score))

    def predict(self, camera_url):
        prediction_thread = threading.Thread(target=self.predict_emotion, args=(camera_url,))
        results_thread = threading.Thread(target=self.process_results)

        prediction_thread.start()
        results_thread.start()

        prediction_thread.join()
        results_thread.join()


