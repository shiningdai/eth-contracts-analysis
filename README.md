# Ethereum Solidity Smart Contract Analysis
首先通过Google BigQuery沙盒获取合约地址（交易量Top20以及交易量超过8000的ERC20和ERC721合约）；
其次通过py-etherscan-api在etherscan上爬取上述合约地址对应的合约源码（仅爬取solidity合约）。
## 1 BigQuery查询合约地址
使用[Google BigQuery沙盒](https://console.cloud.google.com/projectselector2/bigquery?supportedpurview=project)，创建项目，搜索数据集
![image.png](https://intranetproxy.alipay.com/skylark/lark/0/2022/png/65956335/1660791565785-f2e69282-b155-4969-9069-a46bdb94a30f.png#clientId=u211cdba8-7d95-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=542&id=u9bdf638e&margin=%5Bobject%20Object%5D&name=image.png&originHeight=1084&originWidth=2210&originalType=binary&ratio=1&rotation=0&showTitle=false&size=199901&status=done&style=none&taskId=u7fdd2fec-f660-4d10-ab7a-32b847a1d17&title=&width=1105)
![image.png](https://intranetproxy.alipay.com/skylark/lark/0/2022/png/65956335/1660792483307-978c6fe4-3fdb-4376-a702-8161f01073c2.png#clientId=u211cdba8-7d95-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=331&id=ue6d58d9f&margin=%5Bobject%20Object%5D&name=image.png&originHeight=662&originWidth=2194&originalType=binary&ratio=1&rotation=0&showTitle=false&size=151620&status=done&style=none&taskId=ub4e1f0da-572b-41e8-80bc-6d7d2635639&title=&width=1097)
![image.png](https://intranetproxy.alipay.com/skylark/lark/0/2022/png/65956335/1660791843788-79382604-7a95-4f81-8bb7-44b33d5050d9.png#clientId=u211cdba8-7d95-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=427&id=u6b5ed253&margin=%5Bobject%20Object%5D&name=image.png&originHeight=854&originWidth=2220&originalType=binary&ratio=1&rotation=0&showTitle=false&size=256921&status=done&style=none&taskId=uef0ae108-204c-4dc9-a4da-8beed5fd70d&title=&width=1110)

### [Ethereum Cryptocurrency](https://console.cloud.google.com/marketplace/product/ethereum/crypto-ethereum-blockchain?q=search&referrer=search&supportedpurview=project)
Transaction data and more from the Ethereum Blockchain
Google Bigquery 数据库查询以太坊合约的 ERC 721 合约示例 ： 
```plsql
SELECT contracts.address, COUNT(1) AS tx_count
FROM `bigquery-public-data.crypto_ethereum.contracts` AS contracts
JOIN `bigquery-public-data.crypto_ethereum.transactions` AS transactions ON (transactions.to_address = contracts.address)
WHERE contracts.is_erc721 = TRUE
GROUP BY contracts.address
ORDER BY tx_count DESC
LIMIT 10
```
```plsql
SELECT contracts.address, COUNT(1) AS tx_count
FROM `bigquery-public-data.crypto_ethereum.contracts` AS contracts
JOIN `bigquery-public-data.crypto_ethereum.transactions` AS transactions ON (transactions.to_address = contracts.address)
WHERE contracts.is_erc20 = TRUE
GROUP BY contracts.address
ORDER BY tx_count DESC
LIMIT 20
```
![image.png](https://intranetproxy.alipay.com/skylark/lark/0/2022/png/65956335/1660792166889-b341b0c1-0688-4c4c-ab94-7b8dd97bdcd8.png#clientId=u211cdba8-7d95-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=527&id=u6ca49470&margin=%5Bobject%20Object%5D&name=image.png&originHeight=1054&originWidth=2216&originalType=binary&ratio=1&rotation=0&showTitle=false&size=318782&status=done&style=none&taskId=ubeda9fb2-3922-4727-9d1c-207ffe538ba&title=&width=1108)

## 2 分析合约

