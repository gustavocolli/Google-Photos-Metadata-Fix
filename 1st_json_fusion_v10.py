import os
import json
import re
from difflib import SequenceMatcher
from PIL import Image
from pillow_heif import register_heif_opener

# Register HEIC/HEIF support for Pillow
register_heif_opener()

def normalize_name(name):
    """
    Normalize a file name by removing non-alphanumeric characters and converting to lowercase.
    :param name: Original file name
    :return: Normalized file name
    """
    return re.sub(r'[^a-zA-Z0-9]', '', name).lower()

def find_best_match(json_name, media_files):
    """
    Locate the best matching media file for a JSON based on flexible matching rules.
    :param json_name: Name of the JSON file without extension
    :param media_files: List of media files in the directory
    :return: Path of the best matching media file, or None if not found
    """
    normalized_json_name = normalize_name(json_name)
    best_match = None
    highest_similarity = 0

    for media in media_files:
        normalized_media_name = normalize_name(os.path.splitext(media)[0])
        similarity = SequenceMatcher(None, normalized_json_name, normalized_media_name).ratio()
        if similarity > highest_similarity:
            best_match = media
            highest_similarity = similarity

    # Ensure the similarity is high enough to be considered a match
    if highest_similarity >= 0.7:
        return best_match
    return None

def convert_heic_to_jpeg(heic_path):
    """
    Convert a .HEIC image to .jpeg format and move the original file to the 'heic_files' folder.
    :param heic_path: Path to the HEIC file
    :return: Path to the converted JPEG file
    """
    try:
        if not heic_path.lower().endswith(".heic"):
            raise ValueError("File is not a .HEIC file.")

        # Open the HEIC image and convert to RGB
        with Image.open(heic_path) as img:
            img = img.convert("RGB")  # Ensure conversion to RGB
            jpeg_path = f"{os.path.splitext(heic_path)[0]}.jpeg"
            img.save(jpeg_path, "JPEG")
            print(f"Converted {heic_path} to {jpeg_path}.")

            # Create the 'heic_files' folder if it doesn't exist
            heic_folder = os.path.join(os.getcwd(), "heic_files")
            os.makedirs(heic_folder, exist_ok=True)

            # Move HEIC file to 'heic_files' folder
            new_heic_path = os.path.join(heic_folder, os.path.basename(heic_path))
            os.rename(heic_path, new_heic_path)
            print(f"Moved {heic_path} to {new_heic_path}.")

            return jpeg_path
    except Exception as e:
        print(f"Error converting {heic_path} to JPEG: {e}")
        return None

def merge_metadata_directory():
    # Current directory where the script runs
    current_directory = os.getcwd()

    # Create "json_files" folder if it doesn't exist
    json_folder = os.path.join(current_directory, "json_files")
    os.makedirs(json_folder, exist_ok=True)

    # List all files in the directory
    files = os.listdir(current_directory)

    # Filter JSON files
    json_files = [f for f in files if f.lower().endswith('.json')]

    # Filter media files
    media_formats = ['jpg', 'jpeg', 'png', 'mp4', 'mkv', 'avi', 'mov', 'heic']
    media_files = [f for f in files if f.lower().split('.')[-1] in media_formats]

    errors = []  # List to store errors

    for json_file in json_files:
        json_path = os.path.join(current_directory, json_file)

        try:
            # Open and read the JSON file
            with open(json_path, 'r', encoding='utf-8') as f:
                metadata = json.load(f)

            # Locate corresponding media
            base_name = os.path.splitext(json_file)[0]
            corresponding_media = find_best_match(base_name, media_files)

            if corresponding_media is None:
                errors.append(f"{json_file}: Corresponding media file not found (no match above similarity threshold).")
                continue

            media_path = os.path.join(current_directory, corresponding_media)

            print(f"Match found: {json_file} -> {corresponding_media}")

            # Convert HEIC to JPEG if necessary
            if corresponding_media.lower().endswith('.heic'):
                print(f"Attempting to convert {corresponding_media} to JPEG...")
                media_path = convert_heic_to_jpeg(media_path)
                if not media_path:
                    errors.append(f"{json_file}: Failed to convert HEIC to JPEG.")
                    continue

            # Move the JSON file to the "json_files" folder
            new_json_path = os.path.join(json_folder, json_file)
            os.rename(json_path, new_json_path)

            print(f"Metadata from {json_file} successfully incorporated into {media_path}.")

        except Exception as e:
            errors.append(f"{json_file}: Unexpected error - {e}")

    # Display final report
    print("\n--- Final Report ---")
    if errors:
        print("The following JSON files could not be processed:")
        for error in errors:
            print(f"- {error}")
    else:
        print("All JSON files were successfully processed.")

    print(f"\nFiles not processed: {len(errors)}")

if __name__ == "__main__":
    merge_metadata_directory()