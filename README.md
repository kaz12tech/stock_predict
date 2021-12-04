# インストール手順
python version 3.7のconda環境を作成  
$ conda create -n stock_predict python=3.7 jupyter -y  
  
作成した環境をアクティベート  
$ conda activate stock_predict  
$ cd stock_predict  
  
依存するすべてのライブラリを含めてSktimeをインストール  
$ conda install -c conda-forge sktime-all-extras  
  
その他ライブラリをインストール  
$ pip install -r requirements.txt  