import torch

# x = torch.rand(2,2)
# y = torch.rand(2,2)
# y.mul_(x)

# print(y)

# if torch.cuda.is_available():
#     device = torch.device("cuda")
#     x = torch.ones(5, device=device)
#     y = torch.ones(5)
#     y = y.to(device)
#     z = x + y
#     print(z)

x = torch.randn(3, requires_grad=True)
print(x)