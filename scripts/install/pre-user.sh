#!/bin/bash

locale="en_GB.UTF-8"
keyboard="uk"

read -p "Hostname: " hostname

# Setup locale
locale-gen
echo "LANG=$locale" > /etc/locale.conf

# Setup keyboard layout
loadkeys $keyboard
echo "KEYMAP=$keyboard" >> /etc/vconsole.conf

# Setup time
ln -s /usr/share/zoneinfo/Europe/London /etc/localetime

# Setup hooks
hooks="base udev autodetect modconf block encrypt lvm2 btrfs resume filesystems keyboard fsck"
sed 's/^HOOKS\=\".*\"/HOOKS=\"$hooks\"/g' -i /etc/mkinitcpio.conf

# Build kernel
mkinitcpio -p linux

echo $hostname > /etc/hostname

echo "Done. Unmount and reboot."
