import zipfile
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser(description='unzip files')
parser.add_argument('--path', default='/data_object_image_2.zip', help='source zipped files')
parser.add_argument('--tar', default='object/', help='target unzip folder')
args = parser.parse_args()


zip_file = zipfile.ZipFile(args.path)
zip_list = zip_file.namelist() # 得到压缩包里所有文件

for f in tqdm(zip_list):
    zip_file.extract(f, args.tar)
 
zip_file.close()