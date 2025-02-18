import os
import json

# Define paths
human_eval_path = "/Users/deepakshi/Documents/RESULTS Human_eval_xl_indic copy"
llama_path = "/Users/deepakshi/Documents/Human_eval_xl_indic 2 llama 3 7b"

# Iterate through programming languages
for lang in os.listdir(human_eval_path):
    human_lang_path = os.path.join(human_eval_path, lang)
    llama_lang_path = os.path.join(llama_path, lang)
    
    if not os.path.isdir(human_lang_path) or not os.path.isdir(llama_lang_path):
        continue
    
    # Iterate through natural language JSONL files
    for file_name in os.listdir(human_lang_path):
        if not file_name.endswith(".jsonl"):
            continue
        
        human_file = os.path.join(human_lang_path, file_name)
        llama_file = os.path.join(llama_lang_path, file_name)
        
        if not os.path.exists(llama_file):
            print(f"Skipping {human_file}, no matching file in llama folder")
            continue
        
        # Read human_eval JSONL
        with open(human_file, "r", encoding="utf-8") as f:
            human_data = [json.loads(line) for line in f]
        
        # Read llama JSONL
        with open(llama_file, "r", encoding="utf-8") as f:
            try:
                llama_data = {entry["task_id"]: entry.get("instruction_llama_7b", "") for entry in (json.loads(line) for line in f)}
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON in {llama_file}: {e}")
                continue
        
        # Append llama instruction to corresponding human_eval entries
        for entry in human_data:
            task_id = entry.get("task_id")
            if task_id in llama_data and llama_data[task_id]:
                entry["instruction_llama_7b"] = llama_data[task_id]
        
        # Write back updated data
        with open(human_file, "w", encoding="utf-8") as f:
            for entry in human_data:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        
        print(f"Updated {human_file} with llama instructions")

print("Processing complete.")
