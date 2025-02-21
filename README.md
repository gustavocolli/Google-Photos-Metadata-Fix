# Project Overview
This project is not affiliated with Google and has not been officially endorsed. I created a personal initiative to address an issue I faced with Google Photos. My goal is to provide a clear and straightforward guide so that anyone without coding experience can use it effectively and fix the lack of EXIF information in their pictures

# Background
When downloading media from Google, the files usually come with a corresponding .json file which brings EXIF metadata. Unfortunately, this metadata, such as creation date, date taken, media taken and location, is not embedded in the media files. This can be a hassle for those like me who value organized photo and video libraries.

# How to Use This Project
Step 1: Install Python\
Download and install Python from https://www.python.org/downloads/
<pre>
</pre>

Step 2: Install Required Libraries\
Open the Command Prompt on Windows (press Start, type cmd, and hit Enter).\
Run the following commands to install the necessary libraries:

```pip install pillow```

```pip install pillow-heif```

```pip install moviepy```

```pip install piexif```

If you encounter errors running the scripts, you might have installed Python incorrectly. Refer to helpful solutions like this Quora response: https://www.quora.com/My-Python-files-are-not-opening-in-the-terminal-Python-projectfive-py-Why-I-have-tried-several-solutions-but-none-is-working-How-can-I-solve-it
<pre>
</pre>



Step 3: \
→ Download exiftool and ffmpeg folders (available in the download page) and add them to your working folder\
→ Download the Scripts and place them in your working folder:\
\
**For IMAGES:** \
```IMAGE_json_fusion_v10``` \
```IMAGE_convert_heic_to_jpeg_v2``` \
```IMAGE_convert_tif_to_jpeg_v1``` \
\
```1_IMAGE_exif_fixer_from_filename_v11``` \
```2_IMAGE_change_filename_from_filedate_v9``` \
```3_IMAGE_find_identical_pictures_v3``` \

**For VÍDEOS** \
```VIDEO_convert_video_to_mp4_v2``` \
```VIDEO_exif_fixer_from_filename_mp4_v3``` \
```VIDEO_change_filename_from_filedate_v1``` \
<pre>
</pre>

Step 4: Navigate to Your Working Folder\
In the Command Prompt, type: \
```cd C:\path\to\your\folder```
<pre>
</pre>

Step 5: Running the Scripts \
In the Command Prompt, choose the script you would like to use: \
\
**For Images**

```py IMAGE_json_fusion_v10.py``` **(This script pairs .json metadata files with their corresponding images or videos.)** 
```py IMAGE_convert_heic_to_jpeg_v2.py``` **(If you have HEIC files (common on Apple devices), this script converts them to JPEG format.)** 
```py IMAGE_convert_tif_to_jpeg_v1.py``` **(If you have tif files, this script converts them to JPEG format.)** 

```py 1_IMAGE_exif_fixer_from_filename_v11.py``` **(This script updates the Create Date field in EXIF metadata according to the file's name. Rename the file to anything as long as it carries the format DDMMYYY_HHMM or YYYYMMDD_HHMM** \
Example 1: 25122005_1130 - Hiking up the hill.jpg    **(The exif will be changed to 25/12/2005 at 11:30AM)** \
Example 2: IMG 2005.12.25.jpg     **(The exif will be changed to 25/12/2005 but as time was not mentioned, it will be set by default to 12:00)** 

```2_IMAGE_change_filename_from_filedate_v9``` **(This script updates the file name to reflect the Exif. Use it after you have an EXIF sorted out)**
\
Example 1: a file named "- Hiking up the hill.jpg" will be renamed to DDMMYYYY_HHMM - Hiking up the hill.jpg \

```3_IMAGE_find_identical_pictures_v3``` **(This script will move repeated pictures to a new folder inside the working folder)** 

<pre>
</pre>

**For Videos** 
\
```VIDEO_convert_video_to_mp4_v2``` **(Always convert your videos to MP4 before using any other script)** \
```VIDEO_exif_fixer_from_filename_mp4_v3``` **(Same case as explained in the script for images)** \
```VIDEO_change_filename_from_filedate_v1``` **(Same case as explained in the script for images)** \
\
Need Help?
If you happen to have any issues or have questions, feel free to reach out. I’d be happy to assist!

Cheers!
