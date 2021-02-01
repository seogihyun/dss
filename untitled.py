import glob

image_directory = "./Photos/"

extension = "*.jpg"

save_at = "./train.txt"

files = sorted(glob.glob(image_directory + extension))
print(files)

for file in files:
    f = open(save_at, 'a')
    f.write(file + '\n')
    print(file)