#!/bin/bash
echo $'\n1. From which ip were the most requests?'
awk '{print $1}' $1 | sort | uniq -c | sort -gr | head -1

echo $'\n2. What is the most requested page'
awk '{print $7}' $1 | sort | uniq -c | sort -gr | head -1

echo $'\n3. How many requests were there from each ip? '
echo $'\nRequests|  IP'
grep -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}" $1 | sort | uniq -c | sort -gr | head -20

echo $'\n4. What non-existent pages were clients referred to?'
echo $'\nRequests| Page'
awk '{print $7, $9}' $1 | grep " 404" | sort | uniq -c | sort -gr

echo $'\n5. What time did site get the most requests?'
awk -F\: '{print $2":"$3}' $1 | sort | uniq -c | sort -gr | head -1

echo $'\n6. What search bots have accessed the site? (UA + IP)'

echo $'\nFIRST WAY:'
echo $'\nRequests| User Agent'
awk -F\" '{print $6}' $1 | sort | uniq -c | sort -gr | head -20
echo $'\nRequests|     IP     |     User Agent'
awk -F" .* .* \[.*GET.* \"" '{print $1, $2}' $1 | sort | uniq -c | sort -gr | head -20

echo $'\n6. SECOND WAY: (Just searching for "[Bb]ot" in names)'
echo $"(But in this case, we don't get a complete list of user agents)"
echo $'\nRequests| User Agent'
awk '{print $14, $16}' $1 | grep -E -o ".*[bB]ot"  | sort | uniq -c | sort -gr
echo $'\nRequests|     IP     |     User Agent'
awk '{print $1, $14, $16}' $1 | grep -E -o ".*[bB]ot" | sort | uniq -c | sort -gr | head -20
