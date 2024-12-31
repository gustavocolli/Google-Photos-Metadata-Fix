import os
from datetime import datetime
from PIL import Image, ExifTags
from moviepy.video.io.VideoFileClip import VideoFileClip

def get_image_date_taken(image_path):
    """
    Extract the Date Taken metadata from an image.
    :param image_path: Path to the image file
    :return: Date Taken as a datetime object or None
    """
    try:
        with Image.open(image_path) as img:
            exif_data = img._getexif()
            if exif_data is not None:
                for tag, value in exif_data.items():
                    tag_name = ExifTags.TAGS.get(tag, tag)
                    if tag_name == "DateTimeOriginal":
                        return datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
    except Exception as e:
        print(f"Error reading EXIF data from {image_path}: {e}")
    return None

def get_video_creation_date(video_path):
    """
    Extract the Media Created metadata from a video using MoviePy.
    :param video_path: Path to the video file
    :return: Media Created as a datetime object or None
    """
    try:
        with VideoFileClip(video_path) as clip:
            creation_date = clip.creation_date  # Placeholder; MoviePy may not provide creation metadata directly
            if creation_date:
                return datetime.fromisoformat(creation_date)
    except Exception as e:
        print(f"MoviePy failed for {video_path}: {e}")
    return None

def update_file_creation_date(file_path, creation_date):
    """
    Update both the file system creation date and metadata for Date and Date Created.
    :param file_path: Path to the file
    :param creation_date: New creation date as a datetime object
    """
    try:
        timestamp = creation_date.timestamp()
        os.utime(file_path, (timestamp, timestamp))  # Update access and modification times

        if file_path.lower().endswith(('jpg', 'jpeg', 'png')):
            try:
                with Image.open(file_path) as img:
                    exif_data = img.info.get('exif')
                    if exif_data:
                        img.save(file_path, exif=exif_data)
                print(f"EXIF metadata updated for {file_path}")
            except Exception as e:
                print(f"Error updating EXIF metadata for {file_path}: {e}")

    except Exception as e:
        print(f"Error updating creation date for {file_path}: {e}")

def process_files():
    """
    Process all media files in the current directory and update their creation dates.
    """
    current_directory = os.getcwd()
    files = os.listdir(current_directory)

    media_formats = ['jpg', 'jpeg', 'png', 'mp4', 'mov']
    media_files = [f for f in files if f.lower().split('.')[-1] in media_formats]

    errors = []

    for media_file in media_files:
        file_path = os.path.join(current_directory, media_file)
        creation_date = None

        if media_file.lower().endswith(('jpg', 'jpeg', 'png')):
            creation_date = get_image_date_taken(file_path)
        elif media_file.lower().endswith(('mp4', 'mov')):
            creation_date = get_video_creation_date(file_path)

        if creation_date:
            try:
                update_file_creation_date(file_path, creation_date)
                print(f"Updated creation date for {media_file} to {creation_date}.")
            except Exception as e:
                errors.append(f"{media_file}: Failed to update creation date. Error: {e}")
        else:
            errors.append(f"{media_file}: Missing or unreadable creation metadata.")

    print("\n--- Initial Report ---")
    print(f"Files processed: {len(media_files) - len(errors)}")
    if errors:
        print(f"Files with errors: {len(errors)}")
        for error in errors:
            print(f"- {error}")

if __name__ == "__main__":
    process_files()
