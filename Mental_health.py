
import ktrain

predictor = ktrain.load_predictor(r'bert_model')
def pred(que):

    return predictor.predict(que)