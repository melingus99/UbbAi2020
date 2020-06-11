import tensorflow as tf
from tensorflow import keras

class Controller():
    def __init__(self,XTrain,YTrain,EPOCHS = 50, BATCH_SIZE = 128, VERBOSE = 1, NB_CLASSES = 10,N_HIDDEN = 397,VALIDATION_SPLIT = 0.2,RESHAPED = 784 ):
        self.XTrain=XTrain
        self.YTrain=YTrain
        self.epochs=EPOCHS
        self.batchSize=BATCH_SIZE
        self.verbose=VERBOSE
        self.nbClasses=NB_CLASSES
        self.nHidden=N_HIDDEN
        self.validationSplit=VALIDATION_SPLIT
        self.reshaped=RESHAPED
        self.model = tf.keras.models.Sequential()


    def createModel(self):
        self.model.add(keras.layers.Dense(self.nHidden,
          input_shape=(self.reshaped,),
          name='dense_layer', activation='relu'))
        self.model.add(keras.layers.Dense(self.nHidden,
                  name='dense_layer_2', activation='relu'))
        self.model.add(keras.layers.Dense(self.nbClasses,
                  name='dense_layer_3', activation='softmax'))
        # Summary of the model.

        self.model.summary()
        self.model.compile(optimizer='SGD',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

    def train(self):
        self.model.fit(self.XTrain, self.YTrain,
          batch_size=self.batchSize, epochs=self.epochs,
          verbose=self.verbose, validation_split=self.validationSplit)

    def evaluate(self,XTest,YTest):
        test_loss, test_acc = self.model.evaluate(XTest, YTest)
        return test_loss,test_acc
