import os
from PIL import Image
from pillow_heif import register_heif_opener
import piexif

# Register HEIC/HEIF support for Pillow
register_heif_opener()

def convert_heic_to_jpeg(heic_path):
    """
    Convert a .HEIC image to .jpeg format and move the original file to the 'heic_convertedtojpeg_files' folder.
    Preserve EXIF metadata during conversion.
    :param heic_path: Path to the HEIC file
    :return: Path to the converted JPEG file or None if conversion fails
    """
    try:
        if not heic_path.lower().endswith(".heic"):
            raise ValueError("File is not a .HEIC file.")

        # Open the HEIC image
        with Image.open(heic_path) as img:
            # Extract EXIF metadata from the HEIC file
            exif_data = img.info.get("exif", None)

            # Convert to RGB
            img = img.convert("RGB")

            # Save as JPEG with preserved EXIF metadata
            jpeg_path = f"{os.path.splitext(heic_path)[0]}.jpeg"
            img.save(jpeg_path, "JPEG", exif=exif_data)
            print(f"Converted {heic_path} to {jpeg_path}.")

            # Create the 'heic_convertedtojpeg_files' folder if it doesn't exist
            heic_folder = os.path.join(os.getcwd(), "heic_convertedtojpeg_files")
            os.makedirs(heic_folder, exist_ok=True)

            # Move HEIC file to 'heic_convertedtojpeg_files' folder
            new_heic_path = os.path.join(heic_folder, os.path.basename(heic_path))
            os.rename(heic_path, new_heic_path)
            print(f"Moved {heic_path} to {new_heic_path}.")

            return jpeg_path
    except Exception as e:
        print(f"Error converting {heic_path} to JPEG: {e}")
        return None

def convert_all_heic_files():
    # Current directory where the script runs
    current_directory = os.getcwd()

    # List all files in the directory
    files = os.listdir(current_directory)

    # Filter HEIC files
    heic_files = [f for f in files if f.lower().endswith('.heic')]

    errors = []  # List to store errors
    successes = []  # List to store successful conversions

    for heic_file in heic_files:
        heic_path = os.path.join(current_directory, heic_file)
        jpeg_path = convert_heic_to_jpeg(heic_path)
        if jpeg_path:
            successes.append(heic_file)
        else:
            errors.append(heic_file)

    # Display final report
    print("\n--- Final Report ---")
    if successes:
        print("The following HEIC files were successfully converted to JPEG:")
        for success in successes:
            print(f"- {success}")
    else:
        print("No HEIC files were successfully converted.")

    if errors:
        print("\nThe following HEIC files could not be processed:")
        for error in errors:
            print(f"- {error}")
    else:
        print("\nAll HEIC files were successfully processed.")

    print(f"\nFiles successfully processed: {len(successes)}")
    print(f"Files not processed: {len(errors)}")

if __name__ == "__main__":
    convert_all_heic_files()
