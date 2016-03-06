#!/bin/bash

echo "Content-type: text/html"
echo ""

echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
echo '<title>Milight CGI</title>'
echo '</head>'
echo '<body>'

  OIFS="$IFS"

  IFS="${IFS}&"
  set $QUERY_STRING
  Args="$*"
  IFS="$OIFS"

  ARGX=""
  ARGY=""
  ARGZ=""

  for i in $Args ;do


        IFS="${OIFS}="
        set $i
        IFS="${OIFS}"

        case $1 in

                zone) ARGX="`echo $2 | sed 's|[\]||g' | sed 's|%20| |g'`"
                       ;;
                cm) ARGY="`echo $2 | sed 's|%20| |g'`"
                       ;;
                var) ARGZ="${2/\// /}"
                       ;;
        esac
  done

  echo 'Done' 
  echo "$(/home/insertyourusername/milight/milight $ARGX $ARGY $ARGZ)"


 
echo '</body>'
echo '</html>'

exit 0

