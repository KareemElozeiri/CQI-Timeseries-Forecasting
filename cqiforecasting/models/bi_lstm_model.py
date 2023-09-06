from .base_nn import BaseNN
from keras.models import Sequential
from keras.layers import Dense, Bidirectional, LSTM
from keras.losses import MeanSquaredError
from keras.optimizers import Adam 


class BiLSTMModel(BaseNN):

    def __init__(self, input_seq_length, cfg, n_features=1):
        super().__init__(cfg)
        
        self._description = "Double layer LSTM neural net"

        self._seq_length = input_seq_length
        self._n_features = n_features

        self._LSTM1_units = 25
        self._LSTM2_units = 25


    def load_data(self):
        self.X_train, self.X_val, self.X_test, self.y_train, self.y_val, self.y_test = self.data_loader.load_sequences(self._seq_length)

    def build(self):
        self._model = Sequential()
        #adding layers
        self._model.add(Bidirectional(LSTM(self._LSTM1_units, input_shape=(self._seq_length, self._n_features),activation="relu",return_sequences=True)))
        self._model.add(Bidirectional(LSTM(self._LSTM2_units, activation="relu")))
        self._model.add(Dense(1))
    
    def compile(self):
        loss = MeanSquaredError()
        optimizer = Adam()
        self._model.compile(loss=loss, optimizer=optimizer, metrics=["mae"])

    def train(self, batch_size, epochs):
        self._model.compile()
        history = self._model.fit(self.X_train, self.y_train, batch_size=batch_size, epochs=epochs, validation_data=(self.X_val, self.y_val))

        return history

    def evaluate(self):
        eval = self._model.evaluate(self.X_test, self.y_test)

        return eval
