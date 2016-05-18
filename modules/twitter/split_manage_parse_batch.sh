#!/bin/bash 
start=`date +%s.%N`
cd $1 #TODO change this to the location of the raw tweets
dir=$PWD # Used as a reference throughout this script
parentdir="$(dirname "$dir")" # Used to create a new folder in the parent directory of PWD
if [ ! -d $parentdir/parsed-data ]; then
    mkdir $parentdir/parsed-data
fi

g="$(basename $2 .csv)" # Variable for each file, ex: '~/Data/Tests/151230__.csv' becomes '151230'
h=$dir/"$g"_dir # Directory name to be created for each orginial file, ex: '~/Data/Tests/file1a_dir/
mkdir $h # Create directory for each original file; split files will be stored here
split -l 570000 $2 $h/"$g"_split_ # Split each file into x peices to keep from running out of memory. 1 GB ~ 570,000 lines
for j in $h/"$g"_split_??; do
    k="$j"_cleaned.csv # Create variable for cleaned (null bytes removed) file 
    l="$j"_parsed.csv # Create variable for parsed file
    m="$j"_dups_rem.csv # Create variable for duplicates removed file
    python ~/scripts/others/remove_null_fn.py $j $k  # Remove null bytes (these make the parser crash for some reason)
    python ~/scripts/others/parse_tweets_fn.py $k $l # Parse tweets
    awk -v p=$m -F, 'seen[$0]++{next}{print $0 > p}' $l  # Remove duplicates
    rm $j # Remove the original 'split' file - we have no need for it now since the tweets are parsed and the original data are still available
    rm $k # Remove the cleaned split file - these files will take up way too much space
    rm $l # Remove the parsed tweets file with duplicates
done
header="$(head -n -1 $m | head -1)" # Create variable for header
tail -n +2 -q "$h"/*.csv >> "$h"/"$g" # Append csv's together, be sure not to repeat header, name this file after the variable $g
echo $header | cat - $h/$g > temp && mv temp $h/$g # Append header to the file
rm $h/*.csv # Remove individual files with .csv extension, our newly created file does not have this extension
mv $h/$g $h/"$g".csv        
mv $h/"$g".csv $parentdir/parsed-data/ # Move data to parsed data folder 
rm -r $h # Remove the created directory of each orginal file (be careful here)
end=`date +%s.%N`
runtime=$( echo "$end - $start" | bc -l )
echo $runtime > $dir/runtime.txt
