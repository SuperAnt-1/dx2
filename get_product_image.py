import os
import unicodedata

class LocalImageFinder:
  """Finds and returns the path of an image in a local directory."""
  
  def __init__(self, image_directory="/home/yanai-lab/ma-y/www/dx2/images"):
    # IMPORTANT: The absolute path to the image folder. Modify as needed.
    self.image_directory = image_directory
    self.is_valid = os.path.isdir(self.image_directory)

  def find(self, search_name: str):
    """
    Finds an image where its filename is contained within the search_name.
    
    Returns:
      str: The full path to the image if found, otherwise the string "Failed".
    """
    if not self.is_valid or not search_name:
      return "Failed"

    # Normalize strings to prevent encoding-related match failures.
    normalized_search_name = unicodedata.normalize('NFC', search_name.lower())
    
    try:
      for filename in os.listdir(self.image_directory):
        file_basename, _ = os.path.splitext(filename)
        normalized_file_basename = unicodedata.normalize('NFC', file_basename.lower())
        
        # --- LOGIC CHANGE ---
        # Check if the filename is a substring of the input name.
        if normalized_file_basename in normalized_search_name:
          return os.path.join(self.image_directory, filename)
          
    except Exception:
      return "Failed"
      
    return "Failed"

# --- Example Usage ---
if __name__ == "__main__":
  finder = LocalImageFinder()

  if not finder.is_valid:
      print(f"Error: Image directory does not exist -> {finder.image_directory}")
  else:
      # A list of names to test the new finder logic
      names_to_find = [
          "ストロベリー",              # Exact match
          "Mini Cup バニラ",         # Partial match
          "チーズ"                   #failed match 
      ]
      
      for name in names_to_find:
        result = finder.find(name)
        print(f"Searching for: {name}")
        print(f"Output: {result}")