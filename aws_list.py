directories = []
with open("result.txt", "r") as f:
    s3_files = f.readlines()
    pathes = [line.strip().split()[3] for line in s3_files]
    for path in pathes:
        directories.append("/".join(path.split("/")[:2]))

directories = "\n".join(sorted(set(directories)))

with open("directories.txt", "w") as f:
    f.write(directories)