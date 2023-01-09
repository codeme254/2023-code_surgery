# Creates all files necessary for a new problem
#
if [ -z "$1" ]; then
	echo "Please enter directory name"
	echo "Run ./start.sh dirname"
else
mkdir $1
cd $1

echo ""
echo "==================="
echo"Generating new files"


touch problem.txt
touch bruteforce.py
touch optimized_solution1.py
touch optimized_solution2.py
chmod a+x bruteforce.py
chmod a+x optimized_solution1.py
chmod a+x optimized_solution2.py
echo "#!/usr/bin/env python3" > bruteforce.py
fi
