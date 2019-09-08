from keras.utils import plot_model
from keras.models import Model
from keras.layers import Input
from keras.layers import Dense

visible = Input(shape=(10,))
hidden1 = Dense(10)(visible)
hidden2 = Dense(20)(hidden1)
hidden3 = Dense(10)(hidden2)
output = Dense(1)(hidden3)
model = Model(inputs=visible, outputs=output)

# summarize layers
model.summary()

# plot graph
plot_model(model, to_file= ' multilayer_perceptron_graph.png ' )