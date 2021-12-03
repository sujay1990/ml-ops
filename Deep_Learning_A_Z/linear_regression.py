import torch
import torch.nn as nn
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
from torch.nn.modules.container import ModuleList

# prepare datasets

X_numpy, y_numpy = datasets.make_regression(n_samples=100, n_features=1, noise=20, random_state=1)

X = torch.tensor(X_numpy.astype(np.float32))
y = torch.tensor(y_numpy.astype(np.float32))

y = y.view(y.shape[0], 1)


n_samples, n_features = X.shape

 # 1) model
input_size = n_features
output_size = 1
model = nn.Linear(input_size, output_size)

# 2 ) loss and optimizer
learning_rate = 0.01

criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

# 3 ) training loop
num_epoch = 100
for epoch in range(num_epoch):
    # forward pass

    y_pred = model(X)
    loss = criterion(y_pred, y)

    # backward pass

    loss.backward()

    #update

    optimizer.step()

    #empty weights

    optimizer.zero_grad()

    if (epoch+1) % 10 ==0:
        print(f'epoch: {epoch+1}, loss = {loss.item():.4f}')

# plot

predicted = model(X).detach().numpy()

plt.plot(X_numpy, y_numpy, 'ro')
plt.plot(X_numpy, y_numpy, 'b')
plt.show()