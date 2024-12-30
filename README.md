Project Overview
This project is not affiliated with Google and has not been officially endorsed by them. It is a personal initiative I created to address an issue I faced with Google Photos. My goal is to provide a clear and straightforward guide so that anyone, even without coding experience, can use it effectively.

Background
When downloading media from Google, the files usually come with a corresponding .json file containing EXIF metadata. Unfortunately, this metadata, such as creation date, date taken, and location, is not embedded in the media files themselves. For those like me who value organized photo and video libraries, this can be a hassle.

How to Use This Project
Step 1: Install Python
Download and install Python from https://www.python.org/downloads/.


Step 2: Install Required Libraries
Open the Command Prompt on Windows (press Start, type cmd, and hit Enter).
Run the following commands to install the necessary libraries:
pip install pillow
pip install pillow-heif
pip install moviepy
pip install piexif

If you encounter errors running the scripts, you might have installed Python incorrectly. Refer to helpful solutions like this Quora response: https://www.quora.com/My-Python-files-are-not-opening-in-the-terminal-Python-projectfive-py-Why-I-have-tried-several-solutions-but-none-is-working-How-can-I-solve-it

Step 3: Download the Scripts
Place the following scripts in your working folder:
1st_json_fusion_v10.py
2nd_convert_heic_to_jpeg_v1.py
3rd_date_created_fixer_v5.py

Step 4: Navigate to Your Working Folder
In the Command Prompt, type:
cd C:\path\to\your\folder

Step 5: Run the Scripts
In the Command Prompt, type:
py 1st_json_fusion_v10.py (This script pairs .json metadata files with their corresponding images or videos.)
py 2nd_convert_heic_to_jpeg_v1.py (If you have HEIC files (common on Apple devices), this script converts them to JPEG format.)
py 3rd_date_created_fixer_v5.py (This script updates the Create Date field in EXIF metadata using the Date Taken or Media Taken information. This helps ensure your phone gallery correctly places the files in chronological order)

Need Help?
If you encounter any issues or have questions, feel free to reach out. I’d be happy to assist!

Cheers!
