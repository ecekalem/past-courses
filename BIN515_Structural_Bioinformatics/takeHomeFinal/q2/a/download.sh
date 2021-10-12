for i in `cat pdbid.txt`;
do
	wget --no-check-certificate -t 0 https://files.rcsb.org/download/${i}.pdb
done

