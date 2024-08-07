## USAGE
1. Get images + annotations data:
```shell
# get the training data
wget https://requestor-proxy.figure-eight.com/figure_eight_datasets/open-images/train-images-boxable.csv
wget https://requestor-proxy.figure-eight.com/figure_eight_datasets/open-images/train-annotations-bbox.csv

# get the test data
wget https://requestor-proxy.figure-eight.com/figure_eight_datasets/open-images/test-annotations-bbox.csv
wget https://requestor-proxy.figure-eight.com/figure_eight_datasets/open-images/test-images.csv
```

2. Get the labelmap that maps class labels to class IDs:
```shell
wget https://requestor-proxy.figure-eight.com/figure_eight_datasets/open-images/class-descriptions-boxable.csv
```

3. To download a specific objects:
```shell
cd Download/

python download.py --images={PATH_TO_IMAGE_FILE}.csv --annots={PATH_TO_ANNOTATION_FILE}.csv --objects {SPACE_SEPARATE_OBJECT_NAMES} --dir={OUTPUT_DIR} --labelmap={PATH_TO_LABELMAP}.csv

# example

```python download.py --images=./train-images-boxable.csv --annots=./train-annotations-bbox.csv --objects football --dir=./trainimages --labelmap=./class-descriptions-boxable.csv
```
4. This code was modified from harshilpatel312. 
Additions include downloading the images straight to disk.

Run open-images-full-download-to-disk.

In the main function you can change where you want you images to be stored. Images are stored serially from numbers 0 to length of dataframe.

