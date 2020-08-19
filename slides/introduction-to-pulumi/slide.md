---
marp: true
---
# 次世代構成管理ツール Pulumi 試してみた :+1:

---
# whoami :thinking: 

- Name: 森 早人
  - すべて小1で習得する漢字です
- Birth: 1993/10/24
  - 国際連合デー
- Team: 基盤開発T
  - インフラエンジニア
- Resent Events: 
  - キーボード買いました、スコスコ感がだいぶいい感じ
    - [FILCO Majestouch Stingray](https://amzn.to/3gcRp8m)
  - シーシャにハマっています
    - 週1で、近所の感染対策しっかりしてるお店に

---
# Pulumi とは :wrench:

## 好きな言語でIaCできる！

- CloudFormationやTerraformのような、IaCツール。

- 複数言語（JavaScript、Python、TypeScript、Go、C#）で、
AWS、Azure、GCP、K8s上にリソースを構築できる。



![bg width:600px right](./pics/pulumi-2-0.png)

[公式ページ](https://www.pulumi.com/)

---

# インストールとプロジェクトの作成

macOSにて

```sh
## CLIをインストール
$ brew install pulumi 

## プロジェクトを作ると、ログインが求められる。
$ pulumi new aws-python
Manage your Pulumi stacks by logging in.
Run `pulumi login --help` for alternative login options.
Enter your access token from https://app.pulumi.com/account/tokens
    or hit <ENTER> to log in using your browser                   : 
We've launched your web browser to complete the login process.

Waiting for login to complete...
```

--- 

# プロジェクトの情報を入力する

新しく作るプロジェクトの入力が求められる

```sh
project name: (quickstart) 
project description: (A minimal AWS Python Pulumi program) 
Created project 'quickstart'

Please enter your desired stack name.
To create a stack in an organization, use the format <org-name>/<stack-name> (e.g. `acmecorp/dev`).
stack name: (dev) 
Created stack 'dev'

aws:region: The AWS region to deploy into: (us-east-1) ap-northeast-1
Saved config
```


---

# 作られたプロジェクトを確認してみる

S3を作るファイル

```python
#__main.py__

"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3

# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket('my-bucket')

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)

```

---

```
$ pulumi up
Previewing update (dev):
     Type                 Name            Plan       
 +   pulumi:pulumi:Stack  quickstart-dev  create     
 +   └─ aws:s3:Bucket     my-bucket       create     
 
Resources:
    + 2 to create

Do you want to perform this update?  [Use arrows to move, enter to select, type to filter]
> yes
  no
  details
```

---

# 機能

- ダッシュボード
- 
---

# 料金

---

# まとめ

- 
