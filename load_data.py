import torch
import torchvision
from torchvision import transforms
from torch.utils.data import DataLoader
from torch.utils.data.sampler import SubsetRandomSampler
import numpy as np
from sklearn.model_selection import train_test_split

from preprocess import base_dir
dm = base_dir + '/dm/'
valid_size = 0.1


ts = transforms.Compose([transforms.ToTensor(),transforms.Resize((224,224))])

train_dataset = torchvision.datasets.ImageFolder(dm,transform=ts)

train,test = train_test_split(train_dataset,test_size=0.3,shuffle=True)

# shuffle = True
# num_train = len(train_dataset)
# indices = list(range(num_train))
# split = int(np.floor(valid_size * num_train))
# # if shuffle:
# #     np.random.seed(random_seed)
# #     np.random.shuffle(indices)
#
# train_idx, valid_idx = indices[split:], indices[:split]
# train_sampler = SubsetRandomSampler(train_idx)
# valid_sampler = SubsetRandomSampler(valid_idx)
# train_sampler = SubsetRandomSampler(train_idx)
# valid_sampler = SubsetRandomSampler(valid_idx)

train_loader = DataLoader(train,batch_size=1,shuffle=True)


train_features, train_labels = next(iter(train_loader))
print(f"Feature batch shape: {train_features.size()}")
print(f"Labels batch shape: {train_labels}")