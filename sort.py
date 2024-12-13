import re

def sort_json_filenames(filenames):
    """
    Sort filenames of the format 'Chapter_X.json' or 'Chapter_X+subpart.json'.

    :param filenames: List of filenames to sort.
    :return: Sorted list of filenames.
    """
    def parse_filename(filename):
        # Use regex to extract the chapter number and the subpart
        match = re.match(r"Chapter_(\d+)(.*)\\.json", filename)
        if match:
            chapter_number = int(match.group(1))  # Extract chapter number
            subpart = match.group(2)             # Extract subpart (e.g., '+Bitmap_Specifications')
            return chapter_number, subpart
        return float('inf'), filename  # If not matching, put at the end

    # Sort by chapter number and subpart
    return sorted(filenames, key=parse_filename)

# Sample filenames from the images
filenames = [
    "Chapter_1.json",
    "Chapter_2.json",
    "Chapter_2+Bitmap_Specifications.json",
    "Chapter_2+Constructing_Message_Header.json",
    "Chapter_3.json",
    "Chapter_4.json",
    "Chapter_4+Field_2.json",
    "Chapter_4+Field_9.json"
]

# Sort filenames
sorted_filenames = sort_json_filenames(filenames)

# Display sorted filenames
print("\n".join(sorted_filenames))
