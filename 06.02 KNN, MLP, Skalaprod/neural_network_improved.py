import math
import numpy as np
from random import seed
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# Aktivierungsfunktionen und ihre Ableitungen
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return np.where(x > 0, 1, 0)

def tanh(x):
    return np.tanh(x)

def tanh_derivative(x):
    return 1 - np.tanh(x) ** 2

# Künstliches neuronales Netzwerk mit Bias
class NeuralNetwork:
    def __init__(self, i_neurons, h_neurons, o_neurons, learning_rate=0.1, epochs=200, activation="sigmoid", random_state=None, verbose=True):
        self.input_neurons = i_neurons
        self.hidden_neurons = h_neurons
        self.output_neurons = o_neurons
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.categories = []
        self.random_state = random_state
        self.verbose = verbose

        if self.random_state:
            np.random.seed(self.random_state)
            seed(self.random_state)

        # Aktivierungsfunktion auswählen
        self.set_activation_function(activation)

        # Gewichte als Zufallswerte initialisieren ([-0.5, 0.5])
        self.input_to_hidden = np.random.rand(self.hidden_neurons, self.input_neurons) - 0.5
        self.hidden_to_output = np.random.rand(self.output_neurons, self.hidden_neurons) - 0.5

        # Bias-Werte initialisieren ([-0.5, 0.5])
        self.bias_hidden = np.random.rand(self.hidden_neurons, 1) - 0.5
        self.bias_output = np.random.rand(self.output_neurons, 1) - 0.5

    def get_params(self):
        return {"input_neurons":self.input_neurons,
        "hidden_neurons": self.hidden_neurons,
        "output_neurons": self.output_neurons,
        "learning_rate": self.learning_rate,
        "epochs": self.epochs,
        "categories": self.categories,
        "random_state": self.random_state,
        "verbose": self.verbose}
    
    def set_activation_function(self, activation):
        if activation == "sigmoid":
            self.activation = sigmoid
            self.activation_derivative = sigmoid_derivative
        elif activation == "relu":
            self.activation = relu
            self.activation_derivative = relu_derivative
        elif activation == "tanh":
            self.activation = tanh
            self.activation_derivative = tanh_derivative
        else:
            raise ValueError("Unbekannte Aktivierungsfunktion. Verfügbare Optionen: 'sigmoid', 'relu', 'tanh'.")

    def prepare(self, data, labels, test_ratio=0.2):
        scaler = MinMaxScaler()
        data = scaler.fit_transform(data)

        self.categories = list(set(labels))
        y_spread = np.zeros((len(labels), len(self.categories)))
        for i, label in enumerate(labels):
            y_spread[i, self.categories.index(label)] = 1

        if self.random_state:
            x_train, x_test, y_train, y_test = train_test_split(data, y_spread, test_size=test_ratio, random_state=self.random_state)
        else:
            x_train, x_test, y_train, y_test = train_test_split(data, y_spread, test_size=test_ratio)
        return x_train, y_train, x_test, y_test

    def fit(self, inputs, targets):  # train -> fit
        for ep in range(self.epochs):
            for i, (inp, target) in enumerate(zip(inputs, targets), 1):
                
                if self.verbose:
                    print(f"\rEpoch {ep}: Fortschritt {i}/{len(inputs)}", end="")
                
                inp = np.array(inp, ndmin=2).T
                target = np.array(target, ndmin=2).T

                # Forward Propagation mit Bias
                hidden_in = np.dot(self.input_to_hidden, inp) + self.bias_hidden
                hidden_out = self.activation(hidden_in)

                output_in = np.dot(self.hidden_to_output, hidden_out) + self.bias_output
                output_out = self.activation(output_in)

                # Fehlerberechnung
                output_error = target - output_out
                hidden_error = np.dot(self.hidden_to_output.T, output_error)

                # Backpropagation: Berechnung der Gradienten und Aktualisierung der Gewichte & Bias
                self.hidden_to_output += self.learning_rate * np.dot(
                    output_error * self.activation_derivative(output_out), hidden_out.T
                )
                self.bias_output += self.learning_rate * (output_error * self.activation_derivative(output_out))

                self.input_to_hidden += self.learning_rate * np.dot(
                    hidden_error * self.activation_derivative(hidden_out), inp.T
                )
                self.bias_hidden += self.learning_rate * (hidden_error * self.activation_derivative(hidden_out))
                
            if self.verbose:
                print()

    def predict(self, inputs, targets=None):
        results = []
        for inp in inputs:
            inp = np.array(inp, ndmin=2).T
            hidden_out = self.activation(np.dot(self.input_to_hidden, inp) + self.bias_hidden)
            output_out = self.activation(np.dot(self.hidden_to_output, hidden_out) + self.bias_output)
            results.append(self.categories[np.argmax(output_out)])

        if targets is None:
            return results

        correct = sum(1 for res, target in zip(results, targets) if self.categories[np.argmax(target)] == res)
        percent = correct / len(results) * 100
        return correct, percent, results

# Hauptprogramm mit Bias
if __name__ == '__main__':

    iris = load_iris()
    x_data, y_data = iris.data, iris.target

    model = NeuralNetwork(4, 10, 3, learning_rate=0.0005, epochs=2000, activation="tanh", random_state=42)
    x_train, y_train, x_test, y_test = model.prepare(x_data, y_data)
    model.fit(x_train, y_train)  # train -> fit

    correct, percent = model.predict(x_test, targets=y_test)
    print(f"{correct} korrekte Vorhersagen ({percent:.2f}%).")
    
