import json
import os
import sys
os.chdir(sys.path[0])

def get_source_code():
    root_dir = "..\\..\\contracts\\json-info"
    root_save_dir = "..\\..\\contracts\\source-code"
    sub_dirs = os.listdir(root_dir)
    for sub_dir in sub_dirs:
        paths = os.listdir(os.path.join(root_dir, sub_dir))
        for path in  paths:
            files = os.listdir(os.path.join(root_dir, sub_dir, path))
            for file in files:
                file_path = os.path.join(root_dir, sub_dir, path, file)
                with open(file_path) as fp:
                    content = json.loads(fp.read())
                    code = content['SourceCode']
                    name = "%s.sol"% (file[:-5])
                    save_path = os.path.join(root_save_dir, sub_dir, path)
                    if not os.path.exists(save_path):
                        os.mkdir(save_path)
                    code_path = os.path.join(root_save_dir, sub_dir, path, name)
                    with open(code_path, 'w', encoding='utf-8') as fd:
                        fd.write(code)

def main():
    get_source_code()

if __name__ == "__main__":
    main()

        