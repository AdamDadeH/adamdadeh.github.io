#!/bin/bash

# It will stop parsing on the first non-option argument (a string that doesn't begin with a hyphen 
# (-) that isn't an argument for any option in front of it). It will also stop parsing when it sees the -- (double-hyphen)

# OPTIND - current index, is initially set to 1, and needs to be re-set to 1 if you want to parse anything again with getopts
# OPTARG - argument of option
# OPTERR - 1/0 should display error messages

# getops OPTSTRING VARNAME ARGS

# OPTSTRING indicates expected option names
# If we want -f, -A, -x then we have
# getopts fAx VARNAME
# For any option requiring value place a : after the character
# fA:x , A requires a value
# VARNAME - where to place the key-name for argument

# Example of a single argument taking a value. We exit if an illegal argument is passed and
# if -a has no value passed to it.
# getopts_args.sh -a
# getopts_args.sh -a cats
# getopts_args.sh -b
# all behave as expected
# BUT : getopts_args.sh -a -b
# sets a = -b
# Even if b is set as an expected arg... getopts is out.
while getopt "a:b" opt; do
  case $opt in
    a)
      echo "a = $OPTARG" >&2
      ;;
    \?) #getopts handles its own errors - getops does not error out.
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    b)
      echo "b flag on" >&2 ;;
    :) 
      echo "Option $OPTARG requires an argument" >&2
      exit 1
  esac
  done
  shift `expr $OPTIND - 1` 
  echo $1
