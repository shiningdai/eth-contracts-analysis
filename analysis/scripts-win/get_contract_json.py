import os
from etherscan.contracts import Contract
import json
import sys
os.chdir(sys.path[0])


def get_contracts():
    TOKEN = '9FGJN1C5FKQSZRX3RWSZNZUSCVS7TZZF58'
    not_valid = []
    if os.path.exists('not_valid.json'):
        with open('not_valid.json') as fd:
            not_valid = json.load(fd)
    count = 0
    count_effective = 0
    empty = 0
    start = 0
    count_handled = 0
    if len(sys.argv) > 2:
        start = int(sys.argv[2])
    # nb_contracts = 10000
    # address_dir = '..\..\contract-address\ContractAddressERC20-Top20.csv'
    # address_dir = '..\..\contract-address\ERC20ContractAddress8000.csv'
    # address_dir = '..\..\contract-address\ContractAddressERC721-Top20.csv'
    address_dir = '..\..\contract-address\ERC721ContractAddress8000.csv'
    with open(address_dir) as fp:
        line = fp.readline()
        while line:
            count_handled += 1
            address = line.split(',')[0]
            if address == 'address':
                line = fp.readline()
                continue
            count += 1
            if start > count:
                line = fp.readline()
                continue
            if address in not_valid:
                line = fp.readline()
                continue
            try:
                api = Contract(address=address, api_key=TOKEN)
                sourcecode = api.get_sourcecode()
                if len(sourcecode[0]['SourceCode']) == 0:
                    empty += 1
                comp_version = sourcecode[0]['CompilerVersion'][:7]
                if comp_version == "":
                    # contract_dir = '..\\..\\contracts\\json-info\\erc20-8000\\unknown-version'
                    contract_dir = '..\\..\\contracts\\json-info\\erc721-8000\\unknown-version'
                    # contract_path = '..\\..\\contracts\\json-info\\erc20-8000\\unknown-version\\%s.json'(address)
                    contract_path = '..\\..\\contracts\\json-info\\erc721-8000\\unknown-version\\%s.json'(address)
                else:
                    # contract_dir = '..\..\contracts\json-info\erc20-8000\%s' % (comp_version)
                    contract_dir = '..\..\contracts\json-info\erc721-8000\%s' % (comp_version)
                    # contract_path = '..\..\contracts\json-info\erc20-8000\%s\%s.json' % (comp_version, address)
                    contract_path = '..\..\contracts\json-info\erc721-8000\%s\%s.json' % (comp_version, address)
                # 相同版本的合约放到同一目录下
                if not os.path.exists(contract_dir):
                    os.mkdir(contract_dir)
                
                if os.path.exists(contract_path):
                    line = fp.readline()
                    continue
                count_effective += 1
                # print(count, '/', nb_contracts, round(count_effective * 100 / nb_contracts,
                # 2), '%', 'empty', empty, round(empty*100/count_effective, 2), '%')
                
                # contract_path = comp_version + contract_path
                # 'v0.4.19..\\..\\contracts\\json-info\\0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2.json'
                with open(contract_path, 'w') as fd:
                    json.dump(sourcecode[0], fd)

            except Exception as identifier:
                not_valid.append(address)
                with open('not_valid.json', 'w') as fd:
                    json.dump(not_valid, fd)
                print(identifier)
            line = fp.readline()
            print("count_handled:", count_handled)
            print("count_effective:", count_effective)


def main():
    get_contracts()

if __name__ == "__main__":
    main()