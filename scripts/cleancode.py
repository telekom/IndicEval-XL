import json
import re
import os

def clean_instruction(text):
    """Removes markdown artifacts but preserves newlines and meaningful spaces."""
    if not text:
        return text
    # Remove markdown code block markers like ```java or ```
    cleaned = re.sub(r'```[a-zA-Z]*\n?|```', '', text, flags=re.IGNORECASE)
    
    # Remove extra leading/trailing spaces or tabs but preserve spaces between words
    cleaned = re.sub(r'^[ \t]+|[ \t]+$', '', cleaned)
    
    # Replace multiple newlines with two newlines, ensuring the structure remains intact
    cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)
    
    return cleaned

def process_jsonl_file(input_path, output_path):
    """Reads a JSONL file, cleans each entry, and writes back in JSONL format."""
    try:
        with open(input_path, 'r', encoding='utf-8') as file, open(output_path, 'w', encoding='utf-8') as outfile:
            for line_number, line in enumerate(file, start=1):
                if line.strip():
                    try:
                        data = json.loads(line)

                        # Clean specific fields without modifying structure
                        if 'description' in data:
                            data['description'] = clean_instruction(data['description'])
                        if 'instruction_1_5' in data:
                            data['instruction_1_5'] = clean_instruction(data['instruction_1_5'])
                        if 'instruction_2_0' in data:
                            data['instruction_2_0'] = clean_instruction(data['instruction_2_0'])
                        if 'test' in data:
                            data['test'] = clean_instruction(data['test'])

                        # Convert back to JSON string and write to output
                        outfile.write(json.dumps(data, ensure_ascii=False) + '\n')

                    except json.JSONDecodeError as e:
                        print(f"Error decoding line {line_number}: {e}")

    except Exception as e:
        print(f"Error processing file: {e}")

def main():
    base_path = '/Users/deepakshi/Documents/RESULTS Human_eval_xl_indic copy'
    languages = ['Hindi', 'English', 'tamil', 'Sanskrit', 'Urdu', 'Marathi', 'Punjabi']
    
    # Process each language file
    for lang in languages:
        input_path = os.path.join(base_path, f'ruby1/{lang}.jsonl')
        output_path = os.path.join(os.path.dirname(input_path), f'{lang}1.jsonl')

        process_jsonl_file(input_path, output_path)
        print(f"Processing complete for {lang}. Cleaned data saved to {output_path}")

if __name__ == "__main__":
    main()
