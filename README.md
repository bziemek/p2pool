P2Pool for Litecoin Cash
========================
## https://p2p.minelcc.net/

**Pull requests with more bootstrap nodes are highly encouraged!**

### **UPGRADE POSTPONED: A protocol upgrade (from 3301 to 3302) has been delayed due to issues with the web handler undetected during testing. In the meantime, the branch [litecoin-cash-legacy](https://github.com/bziemek/p2pool-litecoincash/tree/litecoin-cash-legacy) is in production use at p2p.minelcc.net and contains several non-breaking features except Segwit address support. I am very sorry for any inconvenience this may have caused.**

Features/patches included:

* Segwit (P2SH & bech32) address support thanks to [spencerr @ VTC P2Pool](https://github.com/vertcoin-project/p2pool-vtc/commit/c3f9268d248cd0e99db551b6e5e8d9ac49fa2427)!
* Rebased against https://github.com/jtoomim/p2pool (Dec. 27, 2018)
  * Includes Segwit and ASICBoost support!
  * Support for wallets without old `getinfo` command
* [Per-address difficulty calculations](https://github.com/p2pool/p2pool/pull/174)
* Subsidy decimal shifting to support LCC (or other similar coins)

BTC 19DEb3TtwAvZDtPkfypTk9xzsCXptJfxPk

LTC Lc6sv9kuC2LeRL6WKtsvsWdxSxFKZDK8EF

LCC CJVscCw3u8GGnp62z6hZwcZbnzKeEjVbJV

Original Readme
===============

**P2pool installation with pypy -- Windows**


On Windows, pypy is only supported via the Windows Subsystem for Linux (WSL). P2pool on pypy on WSL is much faster than P2pool on
CPython on native Windows. To install WSL, first follow the steps outlined here:


https://msdn.microsoft.com/en-us/commandline/wsl/install_guide


Once you've done that, run bash and follow the rest of the steps below.


**P2pool installation with pypy -- Linux and Windows**


Copy and paste the following commands into a bash shell in order to install p2pool on Windows or Linux.

>sudo apt-get update

>sudo apt-get install pypy pypy-dev pypy-setuptools gcc build-essential git


>wget https://bootstrap.pypa.io/ez_setup.py -O - | sudo pypy
>sudo rm setuptools-*.zip


>wget https://pypi.python.org/packages/source/z/zope.interface/zope.interface-4.1.3.tar.gz#md5=9ae3d24c0c7415deb249dd1a132f0f79
tar zxf zope.interface-4.1.3.tar.gz

>cd zope.interface-4.1.3/

>sudo pypy setup.py install

>cd ..

>sudo rm -r zope.interface-4.1.3*


>wget https://pypi.python.org/packages/source/T/Twisted/Twisted-15.4.0.tar.bz2

>tar jxf Twisted-15.4.0.tar.bz2

>cd Twisted-15.4.0

>sudo pypy setup.py install

>cd ..

>sudo rm -r Twisted-15.4.0*


>git clone https://github.com/jtoomim/p2pool.git

>cd p2pool

>git checkout 1mb_segwit


You'll also need to install and run your bitcoind or altcoind of choice, and edit ~/.bitcoin/bitcoin.conf (or the corresponding file for litecoin or whatever other coin you intend to mine) with your bitcoind's RPC username and password. Launch your bitcoind or altcoind, and after it has finished downloading blocks and syncing, go to your p2pool directory and run


>pypy run_p2pool.py


**jtoomimnet vs mainnet**


If you wish to use the original forrestv btc mainnet instead of jtoomimnet, then replace


>git clone https://github.com/jtoomim/p2pool.git

>cd p2pool

>git checkout 1mb_segwit


above with


>git clone https://github.com/p2pool/p2pool.git

>cd p2pool


Note: The BTC p2pools currently have low hashrate, which means that payouts will be infrequent, large, and unpredictable. As of Feb 2018, blocks are found on jtoomimnet on average once every 25 days, and blocks are found on mainnet on average once every 108 days. Do not mine on BTC p2pool unless you are very patient and can tolerate receiving no revenue for several months.


**Miner setup**


P2pool communicates with miners via the stratum protocol. For BTC, configure your miners with the following information:


>URL: stratum+tcp://(Your node's IP address or hostname):9332

>Worker: (Your bitcoin address)

>Password: x


For Litecoin, replace 9332 with 9327. For Bitcoin Cash, use 9348. For Dash, use 7903.


The mining address must be a regular P2PKH address. Segwit, multisig, and bech32 addresses are not supported. That means an address starting with a 1 for Bitcoin or Bitcoin Cash or an L for Litecoin. If you use an address that p2pool cannot understand, then p2pool will mine to that node's default address instead.


If you wish to modify the mining difficulty, you may add something like "address+4096" after your mining address to set the pseudoshare difficulty to 4096, or "address/65536" to set the actual share difficulty to 65536 or the p2pool minimum share difficulty, whichever is higher. Pseudoshares only affect hashrate statistics, whereas actual shares affect revenue variance and efficiency.


**Firewall considerations**


If your node is behind a firewall or behind NAT (i.e. on a private IP address), you may want to forward ports to your p2pool server. P2pool uses two ports: one for p2p communication with the p2pool network, and another for both the web UI and for stratum communication with workers. For Bitcoin, those ports are 9333 (p2p) and 9332 (stratum/web). For Litecoin, they are 9326 (p2p) and 9327 (stratum/web). For Bitcoin Cash, they are 9349 (p2p) and 9348 (stratum/web).
