import matplotlib.pyplot as plt
import numpy as np
import torch
import random


seed = 0
random.seed(seed)
np.random.seed(seed)
torch.manual_seed(seed)
torch.cuda.manual_seed_all(seed)


class Net(torch.nn.Module):
	def __init__(self, dim, layers, nonlinearity):
		super().__init__()

		self.layers = [torch.nn.Sequential(torch.nn.Linear(dim, dim, bias=False), nonlinearity()) for _ in range(layers)]
		self.fc = torch.nn.Sequential(*self.layers)  # Just for torch to realize there are parameters.

	def forward(self, x):
		activations = []
		for layer in self.layers:
			x = layer(x)
			activations.append(x)
		return activations


def main():
	dim = 500
	layers = 10
	data = torch.randn((1000, dim))
	initializations = {
		"normal-small": ("Small Normal",   lambda t: torch.nn.init.normal_(t, std=0.01)),
		"normal-big":   ("Wide Normal",    lambda t: torch.nn.init.normal_(t, std=1)),
		"zeros":        ("Zeros",          lambda t: torch.nn.init.constant_(t, val=0)),
		"xavier":       ("Xavier",         lambda t: torch.nn.init.normal_(t, std=1 / np.sqrt(dim))),
		"he":           ("Altered Xavier", lambda t: torch.nn.init.normal_(t, std=1 / np.sqrt(dim / 2))),
	}
	nonlinearities = {
		"Sigmoid": torch.nn.Sigmoid,
		"Tanh":    torch.nn.Tanh,
		"ReLU":    torch.nn.ReLU
	}
	for initialization, (initialization_title, initialization_fn) in initializations.items():
		means, stds = {}, {}
		for nonlinearity, nonlinearity_fn in nonlinearities.items():
			net = Net(dim, layers, nonlinearity_fn)
			for parameter in net.parameters():
				initialization_fn(parameter)
			activations = net(data)
			means[nonlinearity] = [a.mean() for a in activations]
			stds[nonlinearity] = [a.std() for a in activations]

			fig, axs = plt.subplots(ncols=layers, figsize=(10, 2.5))
			for i, (activation, ax) in enumerate(zip(activations, axs)):
				ax.hist(activation.detach().cpu().numpy().ravel(), 30, range=(-1, 1))
				ax.set_yticks([])
				ax.set_title(f"Layer {i}")
			fig.suptitle(nonlinearity)
			plt.tight_layout()
			fig.subplots_adjust(top=0.8)
			fig.savefig(f"tmp-nn-init-{initialization}-{nonlinearity}-hist.pdf")

		fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 3))
		for label, mean in means.items():
			if initialization == "normal-big" and label == "ReLU":
				continue
			ax1.plot(mean, "-o", label=label)
		ax1.set_xlabel("Layer")
		ax1.set_title("Activation Mean")
		ax1.legend()
		for label, std in stds.items():
			if initialization == "normal-big" and label == "ReLU":
				continue
			ax2.plot(std, "-o", label=label)
		ax2.set_xlabel("Layer")
		ax2.set_title("Activation Standard Deviation")
		ax2.legend()
		fig.suptitle(initialization_title)
		plt.tight_layout()
		fig.subplots_adjust(top=0.9)
		fig.savefig(f"tmp-nn-init-{initialization}.pdf")


if __name__ == '__main__':
	main()
