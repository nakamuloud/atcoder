user=`sed -n 1p secret`
pw=`sed -n 2p secret`
oj login -u $user -p $pw https://atcoder.jp/
