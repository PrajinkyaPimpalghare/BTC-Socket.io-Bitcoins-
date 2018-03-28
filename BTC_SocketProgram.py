"""============================================================================
INFORMATION ABOUT CODE         Coding: ISO 9001:2015
===============================================================================
Socket programing for getting tickers from BTC server continuously with Asyncio.

Author: Prajinkya Pimpalghare

Date: 29-March-2018
Version: 1.0
Input Variable: OutPutFileName.csv
Basic Requirement websockets ,json and csv.
============================================================================"""
import datetime
import websockets
import asyncio
import json
from six.moves.urllib.parse import urlencode
import time
import csv
import os
import sys


class BtcSocketConnector(object):
    def __init__(self, server, port):
        """
        It holds the initial variables and properties for the code
        :param server:
        :param port:
        """
        self.server = server
        self.port = port
        self.wss_url = 'wss://' + self.server + ':' + str(self.port) + '/socket.io/?' + urlencode(
            {'EIO': 3, 'transport': 'websocket'})
        self.packet = None

    async def socket_connect(self):
        """
        This function will run in async way to get the data from the server and put it in the CSV file.
        """
        async with websockets.connect(self.wss_url) as web_socket:
            self.packet = await web_socket.recv()
            await web_socket.send('42' + '[\"join\", \"Ticker-BTCMarkets-BTC-AUD\"]')
            try:
                while True:
                    try:
                        self.packet = await web_socket.recv()
                        if "42" in self.packet:
                            json_object = json.loads(self.packet.strip("42"))
                            time_stamp = datetime.datetime.utcfromtimestamp(int(json_object[1]['timestamp'])/1000.0).strftime('%Y-%m-%d %H:%M:%S')
                            data = [int(json_object[1]["lastPrice"])/100000000.0, int(json_object[1]["bestBid"])/100000000.0, int(json_object[1]["bestAsk"])/100000000.0]
                            print(time_stamp+" "+str(data[0])+" "+str(data[1])+" "+str(data[2]))
                            with open(FILE_NAME, "a+", newline='') as csv_file:
                                writer = csv.DictWriter(csv_file, fieldnames=['timestamp', 'lastPrice', 'bestBid', 'bestAsk'])
                                writer.writerow(
                                    {"timestamp": time_stamp, "lastPrice": data[0], 'bestBid': data[1],
                                     'bestAsk': data[2]})
                                csv_file.close()
                        web_socket.pong()
                    except:
                        break

            except KeyboardInterrupt:
                web_socket.close()


if __name__ == '__main__':
    try:
        FILE_NAME = sys.argv[1]
    except:
        print("Using Default OutPut File Name : BTCData.csv")
        FILE_NAME = "BTCData.csv"
    SERVER = 'socket.btcmarkets.net'
    PORT = 443
    if not os.path.isfile(FILE_NAME):
        with open(FILE_NAME, "a+", newline='') as csv_file:
            fieldnames = ['timestamp', 'lastPrice', 'bestBid', 'bestAsk']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            csv_file.close()
    while True:
        ROOT = BtcSocketConnector(server=SERVER, port=PORT)
        asyncio.get_event_loop().run_until_complete(ROOT.socket_connect())
