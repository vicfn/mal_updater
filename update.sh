#!/bin/bash

cat > ./send.xml << SAMPLEXML
data=<?xml version="1.0" encoding="UTF-8"?>
<entry>
        <episode>4</episode>
        <status>1</status>
        <score>4</score>
        <downloaded_episodes></downloaded_episodes>
        <storage_type></storage_type>
        <storage_value></storage_value>
        <times_rewatched></times_rewatched>
        <rewatch_value></rewatch_value>
        <date_start></date_start>
        <date_finish></date_finish>
        <priority></priority>
        <enable_discussion></enable_discussion>
        <enable_rewatching></enable_rewatching>
        <comments></comments>
        <fansub_group></fansub_group>
        <tags></tags>
</entry>
SAMPLEXML

echo "Username:"
read username
echo "Password:"
stty -echo
read password
stty echo
echo ""

echo "Attempting to update $username's list..."
#15085 = Amnesia
curl http://myanimelist.net/api/animelist/update/15085.xml -u $username:$password -d @./send.xml 2>/dev/null >/dev/null
sleep 10
rm -f ./send.xml
echo "Done."

