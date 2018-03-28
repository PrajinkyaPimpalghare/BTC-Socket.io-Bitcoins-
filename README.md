# BTC-Socket.io-Bitcoins-
Socket programing for getting tickers from BTC server continuously with Asyncio.
Please refer below link for information about BTC server:
https://github.com/BTCMarkets/API/wiki/websocket

About BTC_SocketProgram.py
----------------------------------
Created by Prajinkya Pimpalghare
----------------------------------
------------------------------------------------------------------------------------------------------
Background:
------------------------------------------------------------------------------------------------------

BTC_SocketProgram.py is an API for fletching data from 'socket.btcmarkets.net' server 
and capturing it into the .csv file. 
It's performance purely depends on the internet speed where the code is running and the load on the 'socket.btcmarkets.net' server.
It fletch the data continously from the server witin few seconds, and this code can be stoped only if internet is down or user manually cancle it.

External Modules Required for the API are: 
websockets,json and csv
which can be installed using PIP:
Command pip install websockets
------------------------------------------------------------------------------------------------------
Usage:
------------------------------------------------------------------------------------------------------

code can be run from the CMD by the below command:
------------------------------------------------------------------------------------------------------
BTC_SocketProgram.py FileNAME.csv 
------------------------------------------------------------------------------------------------------

where FileNAME is the name of the csv file user wants to give.
Instead of file name , file path also can be given.
