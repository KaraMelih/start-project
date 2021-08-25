import argparse, os
parser = argparse.ArgumentParser()

parser.add_argument("-data_loc", "--data_location", help="Data folder name", default='./data/')
parser.add_argument("-img_loc", "--image_location", help="Data folder name", default='./imgs/')

args = parser.parse_args()
data_path = args.data_location
img_path = args.image_location

if data_path[-1] != '/': data_path = data_path+'/'
if img_path[-1]  != '/': img_path = img_path+'/'

print(f"Saving data in    data_path = '{data_path}'")
print(f"Saving images in  img_path  = '{img_path}'")
os.mkdir(data_path) if not os.path.exists(data_path) else None
os.mkdir(img_path) if not os.path.exists(img_path) else None