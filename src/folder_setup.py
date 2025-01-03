import os

def setup_folders():
    """Create the project folder structure."""
    folders = [
        "../data", "../notebooks", "../src", "../logs", "../outputs/cleaned_data"
    ]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    print("Project folders set up.")

if __name__ == "__main__":
    setup_folders()