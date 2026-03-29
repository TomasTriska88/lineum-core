import pytest
import pathlib
import re
import itertools

def check_file_for_czech(filepath):
    # Dictionaries of explicitly allowed words/phrases with diacritics
    allowed_phrases = ["Tomáš Tříska", "Lineum Dynamics s.r.o."]
    
    # Regex to catch typical lowercase and uppercase Czech diacritics
    czech_chars_pattern = re.compile(r'[ěščřžýáíéůúťďňĚŠČŘŽÝÁÍÉŮÚŤĎŇ]')
    violations = []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            # Strip line and remove allowed phrases for checking
            check_line = line
            for phrase in allowed_phrases:
                check_line = check_line.replace(phrase, "")
                
            if czech_chars_pattern.search(check_line):
                # We strip the original line for cleaner output tracking
                violations.append(f"Line {line_num}: {line.strip()}")
                
    return violations

def test_no_czech_in_scripts_directory():
    """
    Ensures that no Python scripts in the 'scripts' directory contain Czech words or characters.
    This enforces the English-only codebase policy for user-facing utility scripts.
    """
    root_dir = pathlib.Path(__file__).parent.parent
    scripts_dir = root_dir / 'scripts'
    
    all_violations = {}
    
    # Check all scripts in 'scripts/' and all python files in root directory
    files_to_check = itertools.chain(scripts_dir.rglob('*.py'), root_dir.glob('*.py'))
    
    for py_file in files_to_check:
        violations = check_file_for_czech(py_file)
        if violations:
            all_violations[py_file.name] = violations
            
    if all_violations:
        error_msg = "Discovered Czech language violations in the following scripts:\n"
        for fname, lines in all_violations.items():
            error_msg += f"\nFile: {fname}\n"
            for line in lines:
                error_msg += f"  - {line}\n"
        pytest.fail(error_msg)
