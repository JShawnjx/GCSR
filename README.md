## Datasets
CT
## How to train GCEDSR (Super-resolution)

Most of the options for image super-resolution are in /src/option.py. You can modify ./src/option.py to change the settings. Then use the following code to train GCEDSR.

 conda install pytorch==1.12.0 torchvision==0.13.0 torchaudio==0.12.0 cudatoolkit=11.3 matplotlib imageio scikit-image tqdm -c pytorch

Or use:

    python ./src/main.py --model GCSR --save_results --save_models

You also can run this project using CPU:

```
python ./src/main.py --model GCSR --save_results --save_models --cpu
```



## Test

To test image super-resolution, use python ./src/main.py --save_results --test_only --resume 

