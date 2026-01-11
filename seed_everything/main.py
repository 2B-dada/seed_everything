import random
import numpy as np

try:
    import torch
    torch_available = True
except ModuleNotFoundError:
    print("Package Pytorch not found.")
    torch_available = False

def seed_everything(random_seed:int=10086):
    random.seed(random_seed)
    np.random.seed(random_seed)

    if torch_available:
        torch.manual_seed(random_seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed(random_seed)
            torch.cuda.manual_seed_all(random_seed)

            torch.backends.cudnn.benchmark = True
            try:
                torch.set_float32_matmul_precision("medium")
            except Exception:
                pass