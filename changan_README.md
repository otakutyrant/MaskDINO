# prerequiste

Linux with Python = 3.8, CUDA = , opencv，python-venv，python-pip

默认工作目录为 /tmp/algorithm，后者被挂载为 seg 算法。后者应该已经自带虚拟环境 `.env`，理论上以下步骤可以跳过。出现版本匹配或其它错误时，可以删掉 `.env` 重新走一遍以下步骤。

在 maskdino-main 目录里部署虚拟环境：`cd maskdino-main; python -m venv .env; source .env/bin/activate`

安装 python 依赖：`pip install -m ../detectron2; pip install -r requirement.txt`

修改 `.env/lib/python3.8/site-packages/detectron2/evaluation/sem_seg_evaluation.py"` 所有 np.int 和 np.float 分别为 int，float

编译 CUDA 模块：`export CUDA_HOME=path/to/cuda; cd maskdino/modeling/pixel_decoder/ops sh make.sh` CUDA_HOME 目录指向 CUDA toolkit，Ubuntu 下一般为 /usr/local/cuda-X.X

## notes

SDA 平台的 docker 容器启动时好像会把 tmp/algorithm 里所有文件改为只可读。确保 .env/bin 里 pip, python 为可执行。也要能正常访问 pip 镜像

如果之后有遇到 import cv2 时导入某 so 失败，说该动态库不存在，则在虚拟环境里 pip install opencv-contrib-python-headless

如果之后遇到缺什么第三方 python 包，就装什么包，比如 pycocotools 或 `git+https://github.com/mcordts/cityscapesScripts.git`

## Example conda environment setup

以下仅作为参考，用的虚拟环境工具是 conda，和上文 prerequiste 里的 venv 不一样。

```
conda create --name maskdino python=3.8 -y
conda activate maskdino
conda install pytorch==1.9.0 torchvision==0.10.0 cudatoolkit=11.1 -c pytorch -c nvidia
pip install -U opencv-python

# under your working directory
git clone git@github.com:facebookresearch/detectron2.git
cd detectron2
pip install -e .
pip install git+https://github.com/cocodataset/panopticapi.git
pip install git+https://github.com/mcordts/cityscapesScripts.git

cd ..
git clone git@github.com:facebookresearch/MaskDINO.git
cd MaskDINO
pip install -r requirements.txt
cd maskdino/modeling/pixel_decoder/ops
sh make.sh
```
