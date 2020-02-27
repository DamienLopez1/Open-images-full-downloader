import wget

# get the training data

url1 = 'https://requestor-proxy.figure-eight.com/figure_eight_datasets/open-images/train-images-boxable.csv'
trainimages = wget.download(url1)

url2 = 'https://requestor-proxy.figure-eight.com/figure_eight_datasets/open-images/train-annotations-bbox.csv'
trainannotations  = wget.download(url2)

# get the test data
url3 = 'https://requestor-proxy.figure-eight.com/figure_eight_datasets/open-images/test-annotations-bbox.csv'
testannotations = wget.download(url3)
url4 = 'https://requestor-proxy.figure-eight.com/figure_eight_datasets/open-images/test-images.csv'
testannotations = wget.download(url4)

#Get the labelmap that maps class labels to class IDs:
url5 =  'https://requestor-proxy.figure-eight.com/figure_eight_datasets/open-images/class-descriptions-boxable.csv'
labelmap = wget.download(url5)
#
#cd /downloader

#python download.py --images={PATH_TO_IMAGE_FILE}.csv --annots={PATH_TO_ANNOTATION_FILE}.csv --objects {SPACE_SEPARATE_OBJECT_NAMES} --dir={OUTPUT_DIR} --labelmap={PATH_TO_LABELMAP}.csv
#python download.py --images=/home/smr/projects/open-images-downloader/test-images.csv --annots=/home/smr/projects/open-images-downloader/test-annotations-bbox.csv --objects boat buoy --dir=/home/smr/projects/open-images-downloader/test --labelmap=/home/smr/projects/open-images-downloader/class-descriptions-boxable.csv
