# インストール手順
python version 3.8のconda環境を作成  
$ conda create -n stock_predict python=3.8 jupyter -y  
  
作成した環境をアクティベート  
$ conda activate stock_predict  
$ cd stock_predict  

作業ディレクトリ作成
$ mkdir workspace && cd workspace  

git clone  
$ git clone https://github.com/kaz12tech/stock_predict.git  
  
sktime[all_extras]に含まれるprophetが利用するpystanのバージョンを明示的に指定してインストール  
sktimeは現状pystan 3以上非サポート  
https://github.com/facebook/prophet  
$ pip3 install pystan==2.19.1.1
  
依存するすべてのライブラリを含めてSktimeをインストール  
$ pip3 install sktime[all_extras]  

yahoo_finance_api2をインストール  
$ pip3 install yahoo_finance_api2  

その他  
$ pip3 install prophet==1.0.1  