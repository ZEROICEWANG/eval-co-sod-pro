from torch.utils import data
import os
from PIL import Image


class EvalDataset(data.Dataset):
    def __init__(self, pred_root, label_root):
        pred_imgs = os.listdir(pred_root)
        label_imgs = os.listdir(label_root)

        self.image_path = list(
            map(lambda x: os.path.join(pred_root, x), pred_imgs))
        self.label_path = list(
            map(lambda x: os.path.join(label_root, x), label_imgs))

    def __getitem__(self, item):
        pred = Image.open(self.image_path[item]).convert('L')
        gt = Image.open(self.label_path[item]).convert('L')
        if pred.size != gt.size:
            pred = pred.resize(gt.size, Image.BILINEAR)
        return pred, gt

    def __len__(self):
        return len(self.image_path)
