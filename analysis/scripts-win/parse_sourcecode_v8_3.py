import json
import os
import sys
os.chdir(sys.path[0])

def get_source_code_v8():
    root_dir = "..\\..\\contracts\\v0.8.x\\erc721"
    sub_dirs = os.listdir(root_dir)
    for sub_dir in sub_dirs:
        files = os.listdir(os.path.join(root_dir, sub_dir))
        for file in files:
            file_path = os.path.join(root_dir, sub_dir, file)
            save_path = os.path.join(root_dir, sub_dir, file[:-5])
            if not os.path.exists(save_path):
                os.mkdir(save_path)
            with open(file_path, encoding='utf-8') as fp:
                content = json.loads(fp.read())
                contracts = content['sources']
                for contr in contracts:
                    print(contr)
                    content = contracts[contr]['content']
                    print(content)
                    name = contr.split('/')[-1]
                    save_file = os.path.join(save_path, name)
                    # code_path = os.path.join(root_save_dir, sub_dir, path, name)
                    with open(save_file, 'w', encoding='utf-8') as fd:
                        fd.write(content)

def main():
    get_source_code_v8()

if __name__ == "__main__":
    main()

        