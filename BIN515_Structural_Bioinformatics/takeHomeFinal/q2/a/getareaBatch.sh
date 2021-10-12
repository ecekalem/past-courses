chainSep="/home/ece/Desktop/structuralBioinformatics/FinalTakeHome/q2/chainSeparator.py"
getArea="/home/ece/Desktop/structuralBioinformatics/FinalTakeHome/q2/Getarea_Remote.pl"
cd pdbfiles
for pdb in `ls *.pdb`;
do
	echo $pdb
	mkdir ${pdb%%.pdb}
	mv $pdb ${pdb%%.pdb}
	cd ${pdb%%.pdb}
	python3 $chainSep $pdb
	echo "finished chainSep for $pdb"
	perl $getArea $pdb ## ASA for the complex
	echo "finished getArea for complex"
	sleep 10

	for chain in `ls *_chain*.pdb`; ## ASA for the chains
	do
		perl $getArea $chain
		sleep 10
	done
	echo "finished getArea for chains"
	
	cd ../
done


