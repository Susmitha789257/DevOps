#!/bin/bash
USER="root"
PASSWORD="Susmitha@789"
DATABASE="Daily_Time_Sheet_2025"

function Daily_Time_Sheet()
{
    echo "WELCOME TO DAILY TIME SHEET PORTAL"
    old=("EXIT PORTAL" "OLD" "NEW" "SYNCED")
    action=("BACK" "TODAY INSERT" "PAST INSERT" "WEEKLY VIEW" "MONTHLY VIEW" "FINAL VIEW")
    level=("BACK" "BASIC" "INTERMEDIATE" "ADVANCED" "EXPERT" "ADDITIONAL")
    entry=("BACK" "LEVEL WISE" "ALL IN ONE" "VIEW RECORD")
}
Daily_Time_Sheet
function Space()
{
  i=$(printf "%-7s" "$1")   # Pad prefix to 7 characters (right-aligned)
  shift                         # Shift to get remaining arguments
  for arg in "$@"; do
    val=$(printf "%-19s" "$arg")  # Pad each arg to 19 characters (left-aligned)
    echo "| $i| $val|"
  done
  i=$((i + 1))
}

function MainMenu1()
{
    echo "+--------+--------------------+"
    echo "| S.NO   |      OLD/NEW       |"
    echo "+--------+--------------------+"
    i=0
    for val in "${old[@]}"; do
      Space "$i" "$val"
    done
    echo "+--------+--------------------+"
    read -p "Please enter your option : " option

}
MainMenu1