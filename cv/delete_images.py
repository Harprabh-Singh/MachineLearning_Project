import os
import glob

# Directories to clean
dirs = ["cv/images/buy", "cv/images/sell", "cv/images/hold"]

# Delete all PNG files in each directory
for dir_path in dirs:
    if os.path.exists(dir_path):
        png_files = glob.glob(os.path.join(dir_path, "*.png"))
        for png_file in png_files:
            os.remove(png_file)
            print(f"Deleted: {png_file}")

print("✅ All generated images deleted.")