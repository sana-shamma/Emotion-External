from ..criteriaDetectionBehavior.detectionBehavior import DetectionBehavior

class UniformDetection(DetectionBehavior):
    
    def detect(self, camera_ID, camera_url):
        print("hi uniform")
        return True