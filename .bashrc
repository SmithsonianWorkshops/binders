# Set the bash prompt
# Example: [jovyan@2dm75l77mi ~]$ 

# The host name of binder instances can be very long, this should remove everything before the last "-" of the $HOSTNAME
SHORTHOST=${HOSTNAME##*-}

# If that fails, use the full hostname
if [ -z $SHORTHOST ]; then
  SHORTHOST=$HOSTNAME
fi

PS1="[\u@$SHORTHOST \W]\$ "
