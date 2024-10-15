from EmotionDetection.emotion_detection import emotion_detector
import unittest


class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
    # Test case 1  "I am glad this happened" dom-> "joy"  
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'],'joy')
    # Test case 2  "I am really mad about this" dom-> "anger" 
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2['dominant_emotion'],'anger')
    # Test case 3  "I feel disgusted just hearing about this" dom-> "disgust" 
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_3['dominant_emotion'],'disgust')
    # Test case 4  "I am so sad about this" dom-> "sadness" 
        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_4['dominant_emotion'],'sadness')
    # Test case 5  "I am really afraid that this will happen" dom-> "fear" 
        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_5['dominant_emotion'],'fear')    


unittest.main()