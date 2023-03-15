<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">PyTorch-Based Evaluation Tool for Co-Saliency Detection with faster speed</h3>
  <p align="center">
    Automatically evaluate 8 metrics and draw 4 types of curves
  </p>
</p>

**This is a update base on eval-co-sod(https://github.com/zzhanghub/eval-co-sod), faster, but need more memory space**
***
**Eval Co-SOD** is an extended version of [Evaluate-SOD](https://github.com/Hanqer/Evaluate-SOD) for **co-saliency detection task**.
It provides eight metrics and four curves:
* Metrics:
    * Mean Absolute Error (MAE)
	* Maximum F-measure (max-Fm)
	* Mean F-measure (mean-Fm)
	* Maximum E-measure (max-Em)
	* Mean E-measure (mean-Em)
	* S-measure (Sm)
	* Average Precision (AP)
	* Area Under Curve (AUC)
* Curves:
	* Precision-Recall (PR) curve
	* Receiver Operating Characteristic (ROC) curve
	* F-measure curve
	* E-measure curve


## Prerequisites
* PyTorch >= 1.0


## Usage

### 1. Prepare your data
The structure of `root_dir` should be organized as follows:
```
.
├── gt
│   ├── dataset1
│   │   ├── 51490.png
│   │   ├── 51491.png
│   │   └── 51492.png
│   ├── dataset2 ...
│   └── dataset3 ...
│ 
└── pred
    └── method1
    │   ├── dataset1
    │   │   ├── 51490.png
    │   │   ├── 51491.png
    │   │   └── 51492.png
    │   ├── dataset2 ..
    │   └── dataset3 ...
    └──method2 ...
```

### 2. Evaluate on the 8 metrices
1. Configure `eval.sh`
```shell
--methods method1+method2+method3 (Multiple items are connected with '+')
--datasets dataset1+dataset2+dataset3
--save_dir ./Result (Path to save results)
--root_dir ../SalMaps
```

2. Run by
```
sh eval.sh
```

### 3. Draw the 4 types of curves
1. Configure `plot_curve.sh`
```shell
--methods method1+method2+method3 (Multiple items are connected with '+')
--datasets dataset1+dataset2+dataset3
--out_dir ./Result/Curves (Path to save results)
--res_dir ./Result/Detail
```

2. Run by
```
sh plot_curve.sh
```
