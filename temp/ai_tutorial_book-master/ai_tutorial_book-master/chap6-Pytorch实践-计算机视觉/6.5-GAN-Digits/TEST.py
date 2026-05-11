import torch
import math
def get_timestep_embedding(
timesteps: torch.Tensor,
embedding_dim: int = 128,
downscale_freq_shift: float = 1,
max_period: int = 10000):
    half_dim = embedding_dim // 2
    exponent = -math.log(max_period) * torch.arange(
        start=0, end=half_dim, dtype=torch.float32)
    exponent = exponent / (half_dim - downscale_freq_shift)
    emb = torch.exp(exponent)
    emb = timesteps[:, None].float() * emb[None, :]
    emb = torch.cat([torch.sin(emb), torch.cos(emb)], dim=-1)
    # zero pad
    if embedding_dim %2 == 1:
        emb = torch.nn.functional.pad(emb, (0, 1, 0, 0))
    return emb

timesteps = torch.Tensor([20,40])
timestepsb = torch.Tensor([[[20],[40]],[[60],[80]]])

a = get_timestep_embedding(timesteps,embedding_dim=5)
b = get_timestep_embedding(timestepsb)
#c = get_timestep_embedding(timestepsc)

print(a.shape, b.shape)