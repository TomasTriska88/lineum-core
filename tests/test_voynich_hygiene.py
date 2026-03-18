import os
import subprocess

def test_voynich_data_git_hygiene():
    """
    Ensures that the generated Voynich JSON payload files are strictly ignored
    by Git to prevent accidental redistribution of proprietary transcribed text.
    """
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    test_file = os.path.join(repo_root, "data", "voynich", "f_dummy_test.json")
    
    # Create the test directory if it doesn't exist
    os.makedirs(os.path.dirname(test_file), exist_ok=True)
    
    # Touch a dummy JSON file
    with open(test_file, 'w') as f:
        f.write('{"test": true}')
        
    try:
        # Check if the file is ignored by Git
        result = subprocess.run(
            ['git', 'check-ignore', test_file],
            cwd=repo_root,
            capture_output=True,
            text=True
        )
        
        # Git check-ignore returns 0 if the file is ignored, 1 if it is NOT ignored.
        assert result.returncode == 0, f"Git hygiene violation! {test_file} is NOT ignored by Git. Check .gitignore rules for data/voynich/*.json."
    finally:
        # Clean up
        if os.path.exists(test_file):
            os.remove(test_file)
