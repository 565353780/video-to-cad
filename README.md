# Video To CAD

## Source

```bash
https://github.com/likojack/ODAM
```

## Download

### ScanNet Dataset

### Pretrained Model

[here](https://drive.google.com/drive/folders/13tpl9j0TGuJjXBCmsyLqHWBque27n-xv?usp=sharing)

```bash
ln -s <path-to-scannet-dataset-folder> ./data
ln -s <path-to-pretrained-model-folder> ./experiments
```

make sure it looks like

```bash
./data/ScanNet/scans/
./experiments/detector.pth
```

## Build

```bash
conda env create -f environment.yml
conda activate odam
pip install cython numba
cd src/super_quadric
python setup.py install
cd ../..
```

## Run

```bash
export PYTHONPATH=$PYTHONPATH:$PWD
python src/scripts/run_processor.py --config_path ./configs/detr_scan_net.yaml --no_code --use_prior --out_dir ./result/e2e --representation super_quadric
```

## Enjoy it~

