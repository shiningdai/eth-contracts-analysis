# Ethereum Solidity Smart Contract Analysis
首先通过Google BigQuery沙盒获取合约地址（交易量Top20以及交易量超过8000的ERC20和ERC721合约）；  
其次通过[py-etherscan-api](https://github.com/corpetty/py-etherscan-api)在[etherscan](https://etherscan.io/)上爬取上述合约地址对应的合约源码（仅爬取solidity合约）。
## 1 BigQuery查询合约地址
使用[Google BigQuery沙盒](https://console.cloud.google.com/projectselector2/bigquery?supportedpurview=project)，创建项目，搜索数据集

![image.png](./introduction-files/figures/create_bigquery_project.png)

![image.png](./introduction-files/figures/search_dataset.png)

![image.png](./introduction-files/figures/sql_query_stmt.png)

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
![image.png](./introduction-files/figures/sql_query_stmt.png)

## 2 分析合约


## Reference
[TxAnalysis](https://github.com/JolyonJian/tx-analysis.git)
